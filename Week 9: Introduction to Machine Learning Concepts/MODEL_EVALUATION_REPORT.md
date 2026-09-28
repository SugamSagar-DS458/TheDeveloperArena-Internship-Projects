# Model Evaluation Report: House Price Prediction

**Selected model:** Gradient Boosting Regressor (scikit-learn)
**Dataset:** `house_prices.csv` (300 rows, no missing values)
**Target:** `Price` (range about 8M to 59M)
**Code:** `house_price_model.py` | **Random seed:** 42

---

## 1. Summary

| Item | Result |
|---|---|
| Test R² | **0.982** |
| Test MAE | **1.09M** (about 4.4% of mean price) |
| Test RMSE | **1.58M** |
| Test MAPE | **4.9%** |
| Cross-validated R² (5-fold, train) | 0.990 ± 0.002 |
| Verdict | Strong predictive accuracy; mild overfitting; errors widen for expensive homes |

The model predicts unseen house prices to within about 5% on average and beats both a linear baseline and a Random Forest on every metric.

---

## 2. Evaluation Design

- **Train/test split:** 80% train (240 rows) / 20% test (60 rows), shuffled with `random_state=42`. The test set was used only once, for final evaluation.
- **Model selection:** 5-fold cross-validation on the training set only, using R² as the criterion.
- **Leakage control:** scaling and one-hot encoding are fitted inside a `Pipeline`, so each CV fold and the test set only see statistics learned from training data.
- **Features:** Area, Bedrooms, Bathrooms, Age (numeric); Location, Property_Type (categorical).

### Metrics used

| Metric | What it tells us |
|---|---|
| **R²** | Share of price variance explained (1.0 is perfect) |
| **MAE** | Average absolute error in price units; easy to interpret |
| **RMSE** | Like MAE but penalises large misses more heavily |
| **MAPE** | Average error as a percentage of the true price |

---

## 3. Model Comparison

### Cross-validation (training set, 5-fold R²)

| Model | Mean | Std |
|---|---|---|
| Linear Regression | 0.950 | 0.011 |
| Random Forest | 0.971 | 0.008 |
| **Gradient Boosting** | **0.990** | **0.002** |

### Test set

| Model | R² | MAE | RMSE | MAPE |
|---|---|---|---|---|
| Linear Regression | 0.941 | 2,188,736 | 2,907,633 | 13.16% |
| Random Forest | 0.973 | 1,474,882 | 1,975,534 | 6.70% |
| **Gradient Boosting** | **0.982** | **1,089,399** | **1,584,329** | **4.92%** |

Gradient Boosting cut MAE by about 50% versus the linear baseline and by about 26% versus Random Forest. It also had the most stable cross-validation scores (lowest std).

---

## 4. Generalisation Check (Train vs Test)

| Model | Train R² | Test R² | Gap | Train MAPE | Test MAPE |
|---|---|---|---|---|---|
| Linear Regression | 0.958 | 0.941 | 0.017 | 12.37% | 13.16% |
| Random Forest | 0.997 | 0.973 | 0.024 | 2.97% | 6.70% |
| Gradient Boosting | 0.999 | 0.982 | 0.017 | 1.71% | 4.92% |

- The R² gap is small for all models (≤ 0.024), so overfitting is **mild**.
- The tree models fit training data far more tightly than test data (MAPE 1.7% vs 4.9% for Gradient Boosting). Expect real-world error to be closer to the test figures.
- Linear Regression is consistent across train and test but **underfits**: about 12–13% error on both, which points to non-linear structure it can't capture.

---

## 5. Error Analysis

Figure: `predictions_vs_actual.png` (predicted vs actual, residuals vs predicted, residual histogram).

- **Calibration:** predictions follow the ideal diagonal across the full price range, with no systematic bias.
- **Residual centring:** residuals are centred on zero.
- **Heteroscedasticity:** the spread of residuals grows with price. Cheap homes are predicted within about ±1M, while errors reach ±2–3M at higher prices.
- **Outliers:** the largest misses, about +5M, are under-predictions of expensive properties. They form the right tail of the residual histogram.

---

## 6. Feature Importance

Figure: `feature_importance.png` (permutation importance on the test set, 30 repeats).

| Feature | Drop in R² when shuffled |
|---|---|
| Area | 1.385 ± 0.241 |
| Location | 0.750 ± 0.115 |
| Bedrooms | 0.074 ± 0.012 |
| Age | 0.017 ± 0.004 |
| Bathrooms | 0.004 ± 0.001 |
| Property_Type | 0.0003 ± 0.0003 |

- **Area** and **Location** account for nearly all predictive power.
- Bedrooms and Age add a small, real signal.
- Bathrooms and Property_Type are effectively noise once the other features are known.

Directional effects from the linear baseline: each extra unit of area adds about 7,560; each bedroom about 1.6M; each year of age lowers price by about 82K. City Center is about 16.7M above Rural, and Suburb about 8.1M above Rural.

---

## 7. Limitations

1. **Small sample.** The test set has only 60 rows, so metrics carry sampling uncertainty. Differences between models are clear, but exact figures may shift on a different split.
2. **Coarse location.** Only three location categories are available; finer geography would likely improve accuracy most.
3. **Limited range.** Area values reach about 5,000 and prices about 59M. Predictions outside this range or for unseen markets are unreliable.
4. **No hyperparameter tuning.** Gradient Boosting used reasonable defaults, not a tuned search.
5. **Percentage error rises at low prices.** MAPE is sensitive to cheaper homes, where a fixed absolute error is a larger share of the price.

---

## 8. Recommendations

- Tune `n_estimators`, `learning_rate`, `max_depth` and `subsample` with `RandomizedSearchCV` to reduce the train/test gap.
- Predict `log(Price)` to stabilise error at high prices.
- Use repeated K-fold CV for more reliable performance estimates on this small dataset.
- Add richer location data (neighbourhood, distance to city centre or transit).
- Consider dropping Bathrooms and Property_Type for a simpler model, and confirm with CV.
- Monitor error by price band if the model is deployed.

---

## 9. Reproducibility

```bash
python house_price_model.py /path/to/house_prices.csv
```

Outputs: `house_price_model.joblib`, `metrics.json`, `predictions_vs_actual.png`, `feature_importance.png`, `model_comparison.png`.
