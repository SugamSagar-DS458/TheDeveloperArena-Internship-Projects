"""House price prediction with scikit-learn.

Pipeline: preprocessing (scale numeric, one-hot categorical) -> regressor.
Compares Linear Regression, Random Forest and Gradient Boosting using
5-fold CV on the training set, then evaluates the best on a held-out test set.
"""
import json
import sys
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_absolute_error, mean_absolute_percentage_error,
                             mean_squared_error, r2_score)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

warnings.filterwarnings("ignore")
SEED = 42
DATA = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/uploads/house_prices.csv"
OUT = "/mnt/user-data/outputs"

# ---------------------------------------------------------------- data
df = pd.read_csv(DATA).drop(columns="Property_ID")
target = "Price"
num_cols = ["Area", "Bedrooms", "Bathrooms", "Age"]
cat_cols = ["Location", "Property_Type"]
X, y = df[num_cols + cat_cols], df[target]

# 80/20 split, stratified-ish by shuffling with fixed seed
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED)
print(f"Train: {len(X_train)} rows | Test: {len(X_test)} rows")

# ---------------------------------------------------------------- EDA
print("\nCorrelation with Price (numeric):")
print(df[num_cols + [target]].corr()[target].drop(target).round(3))
print("\nMean price by Location:\n", df.groupby("Location")[target].mean().round(0))
print("\nMean price by Property_Type:\n", df.groupby("Property_Type")[target].mean().round(0))

# ---------------------------------------------------------------- models
def make_pipe(model, scale=True):
    pre = ColumnTransformer([
        ("num", StandardScaler() if scale else "passthrough", num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ])
    return Pipeline([("pre", pre), ("model", model)])

candidates = {
    "Linear Regression": make_pipe(LinearRegression()),
    "Random Forest": make_pipe(RandomForestRegressor(
        n_estimators=300, random_state=SEED), scale=False),
    "Gradient Boosting": make_pipe(GradientBoostingRegressor(
        n_estimators=200, learning_rate=0.05, max_depth=3, random_state=SEED), scale=False),
}

print("\n5-fold CV R^2 on training set:")
cv_results = {}
for name, pipe in candidates.items():
    s = cross_val_score(pipe, X_train, y_train, cv=5, scoring="r2")
    cv_results[name] = (s.mean(), s.std())
    print(f"  {name:20s} {s.mean():.4f} +/- {s.std():.4f}")

best_name = max(cv_results, key=lambda k: cv_results[k][0])
print(f"\nSelected model (best CV R^2): {best_name}")

# ---------------------------------------------------------------- evaluate
def metrics(model, Xs, ys):
    p = model.predict(Xs)
    return {
        "R2": r2_score(ys, p),
        "MAE": mean_absolute_error(ys, p),
        "RMSE": float(np.sqrt(mean_squared_error(ys, p))),
        "MAPE_%": mean_absolute_percentage_error(ys, p) * 100,
    }

all_test = {}
for name, pipe in candidates.items():
    pipe.fit(X_train, y_train)
    all_test[name] = {"train": metrics(pipe, X_train, y_train),
                      "test": metrics(pipe, X_test, y_test)}

print("\nTest-set metrics (all models):")
print(pd.DataFrame({k: v["test"] for k, v in all_test.items()}).T.round(2))
print("\nTrain-set R^2 (overfit check):")
print({k: round(v["train"]["R2"], 4) for k, v in all_test.items()})

best = candidates[best_name]
preds = best.predict(X_test)
residuals = y_test - preds

# ---------------------------------------------------------------- plots
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
M = 1e6

fig, axes = plt.subplots(1, 3, figsize=(17, 5))
ax = axes[0]
ax.scatter(y_test / M, preds / M, alpha=0.7, edgecolor="white", color="#3266ad")
lim = [min(y_test.min(), preds.min()) / M, max(y_test.max(), preds.max()) / M]
ax.plot(lim, lim, "--", color="#c0392b", label="Perfect prediction")
ax.set(xlabel="Actual price (millions)", ylabel="Predicted price (millions)",
       title=f"Predicted vs Actual - {best_name}")
m = all_test[best_name]["test"]
ax.text(0.04, 0.93, f"R² = {m['R2']:.3f}\nMAE = {m['MAE']/M:.2f}M\nRMSE = {m['RMSE']/M:.2f}M",
        transform=ax.transAxes, va="top", bbox=dict(boxstyle="round", fc="white", ec="#ccc"))
ax.legend(loc="lower right")

ax = axes[1]
ax.scatter(preds / M, residuals / M, alpha=0.7, edgecolor="white", color="#2a9d8f")
ax.axhline(0, ls="--", color="#c0392b")
ax.set(xlabel="Predicted price (millions)", ylabel="Residual (millions)", title="Residuals vs Predicted")

ax = axes[2]
ax.hist(residuals / M, bins=15, color="#e9a03b", edgecolor="white")
ax.axvline(0, ls="--", color="#c0392b")
ax.set(xlabel="Residual (millions)", ylabel="Count", title="Residual distribution")
plt.tight_layout()
plt.savefig(f"{OUT}/predictions_vs_actual.png", dpi=150)
plt.close()

# Feature importance (permutation, on test set, on original columns)
imp = permutation_importance(best, X_test, y_test, n_repeats=30, random_state=SEED, scoring="r2")
imp_df = pd.DataFrame({"feature": X.columns, "importance": imp.importances_mean,
                       "std": imp.importances_std}).sort_values("importance")
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.barh(imp_df.feature, imp_df.importance, xerr=imp_df["std"], color="#3266ad")
ax.set(xlabel="Drop in test R² when feature is shuffled", title=f"Permutation importance - {best_name}")
plt.tight_layout()
plt.savefig(f"{OUT}/feature_importance.png", dpi=150)
plt.close()
print("\nPermutation importance (drop in R^2):")
print(imp_df.sort_values("importance", ascending=False).round(4).to_string(index=False))

# Model comparison
fig, ax = plt.subplots(figsize=(7, 4))
names = list(all_test)
ax.bar(names, [all_test[n]["test"]["R2"] for n in names], color=["#8896ab", "#3266ad", "#2a9d8f"])
ax.set(ylabel="Test R²", title="Model comparison (test set)", ylim=(0, 1.05))
for i, n in enumerate(names):
    ax.text(i, all_test[n]["test"]["R2"] + 0.01, f"{all_test[n]['test']['R2']:.3f}", ha="center")
plt.tight_layout()
plt.savefig(f"{OUT}/model_comparison.png", dpi=150)
plt.close()

# Linear-model coefficients for interpretability
lin = candidates["Linear Regression"]
feat_names = lin.named_steps["pre"].get_feature_names_out()
coefs = pd.Series(lin.named_steps["model"].coef_, index=feat_names)
print("\nLinear regression coefficients (numeric are per 1 std dev):")
print(coefs.round(0).to_string())
# Raw per-unit effects
raw = LinearRegression().fit(pd.get_dummies(X_train, columns=cat_cols), y_train)
print("\nRaw per-unit effects:")
print(pd.Series(raw.coef_, index=pd.get_dummies(X_train, columns=cat_cols).columns).round(0).to_string())

# Save results + model
json.dump({"selected": best_name, "cv": {k: {"mean": v[0], "std": v[1]} for k, v in cv_results.items()},
           "results": all_test}, open(f"{OUT}/metrics.json", "w"), indent=2)
import joblib
joblib.dump(best, f"{OUT}/house_price_model.joblib")
print("\nSaved plots, metrics.json and model.")
