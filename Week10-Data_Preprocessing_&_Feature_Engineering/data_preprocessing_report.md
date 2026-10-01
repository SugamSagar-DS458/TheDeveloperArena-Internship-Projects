# Customer Churn Prediction: Data Preprocessing Report

## 1. Executive Summary
This report provides documentation of the data cleaning, feature engineering, encoding, scaling, and modular pipeline design performed on the `customer_churn.csv` dataset. The objective is to prepare raw customer records into a standardized matrix suitable for machine learning classification models.

---

## 2. Dataset Overview & Initial Schema

### 2.1 Initial Features & Target
The dataset consists of demographic, service, and billing information for telecommunications customers:
* **Target Variable:** `Churn` (Binary: `0` = Retained, `1` = Churned)
* **Identifier:** `CustomerID` (unique identifier)
* **Categorical Features:** `Contract`, `PaymentMethod`, `PaperlessBilling`, `SeniorCitizen`
* **Numerical Features:** `Tenure`, `MonthlyCharges`, `TotalCharges`

### 2.2 Dataset Dimensions
* **Total Instances:** 500 samples
* **Train Split:** 400 samples (80%)
* **Test Split:** 100 samples (20%)
* **Final Processed Feature Dimensions:** 9 features

---

## 3. Detailed Preprocessing Steps

### Step 1: Feature Pruning (Dropping Identifiers)
* **Action:** Dropped `CustomerID` from the feature set.
* **Rationale:** Unique customer IDs carry arbitrary nominal value and do not possess generalizable predictive power. Retaining them would induce data leakage or lead to high-cardinality noise.

### Step 2: Missing Value Imputation & Type Conversion
* **`TotalCharges` Conversion:**
  * In raw telecommunication datasets, `TotalCharges` frequently contains blank whitespace strings representing new customers with 0 tenure.
  * **Transformation:** Applied `pd.to_numeric(..., errors='coerce')` to parse non-numeric entries into `NaN`.
  * **Imputation:** Missing entries (`NaN`) were imputed using `0` via `.fillna(0)`.
* **Binary Indicator Standardization:**
  * **`PaperlessBilling`:** Encoded directly from string categorical (`Yes`/`No`) to integer values (`1`/`0`).
  * **`SeniorCitizen`:** Enforced as standard integer type (`int64`).
  * **`Churn`:** Validated as integer binary target (`0`/`1`).

---

## 4. Exploration of Encoding & Scaling Strategies

Before finalizing the unified end-to-end pipeline, the project explored different encoding and transformation strategies:

### 4.1 Categorical Encoding Approaches
1. **One-Hot Encoding (`pd.get_dummies` / `OneHotEncoder`):**
   * Applied to nominal features: `Contract` and `PaymentMethod`.
   * Configured with `drop_first=True` to eliminate redundant dummy variables and avoid the dummy variable trap (multicollinearity).
   * Resulted in binary indicator flags:
     * `Contract_One year`, `Contract_Two year` (reference: `Month-to-month`)
     * `PaymentMethod_Credit Card`, `PaymentMethod_Electronic Check` (reference baseline)
2. **Label Encoding (`LabelEncoder`):**
   * Encoded categorical categories into arbitrary sequential integers ($0, 1, 2, \dots$).
   * *Limitation:* Can inadvertently imply false ordinal hierarchies to linear and distance-based estimators.
3. **Ordinal Encoding (`OrdinalEncoder`):**
   * Maps ordered categories to integer floats ($0.0, 1.0, 2.0, \dots$). Suitable for ordered factors if an explicit ranking order is provided.

### 4.2 Numerical Scaling Transformations
1. **StandardScaler ($z$-score standardization):**
   $$z = \frac{x - \mu}{\sigma}$$
   * Scaled numerical features (`Tenure`, `MonthlyCharges`, `TotalCharges`, `PaperlessBilling`, `SeniorCitizen`) to have $\mu = 0$ and $\sigma = 1$.
   * Retains outliers and centers distributions, which is optimal for linear classifiers, SVMs, and neural networks.
2. **MinMaxScaler (Normalization):**
   $$x_{\text{scaled}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$
   * Scaled feature distributions strictly into the interval $[0, 1]$. Useful when bounded non-negative ranges are required.

---

## 5. Feature Engineering Experiments

The notebook tested the derivation of 5 domain-specific engineered features:

| Feature Name | Formulation | Handled Edge Cases | Intuition |
| :--- | :--- | :--- | :--- |
| `AvgChargePerTenure` | $\frac{\text{TotalCharges}}{\text{Tenure}}$ | Replaced division-by-zero ($\pm\infty$) with `MonthlyCharges`. | Measures historic charge pacing per unit tenure. |
| `IsLongTermCustomer` | $\mathbb{I}(\text{Tenure} > 24)$ | Binary threshold flag. | Identifies customers past the standard 2-year lifecycle. |
| `MonthlyChargeToTotalChargeRatio` | $\frac{\text{MonthlyCharges}}{\text{TotalCharges}}$ | Replaced $\pm\infty$ with `0`. | Measures proportion of current billing against historical aggregate. |
| `TenureToMonthlyChargeRatio` | $\frac{\text{Tenure}}{\text{MonthlyCharges}}$ | Replaced $\pm\infty$ with `0`. | Evaluates tenure gained relative to pricing tier. |
| `IsHighValueCustomer` | $\mathbb{I}(\text{TotalCharges} > \text{median})$ | Median binary partition. | Flags top 50% revenue contributors. |

---

## 6. End-to-End Production Pipeline (`scikit-learn`)

The final workflow is packaged inside a reusable `ColumnTransformer` and `Pipeline` structure to prevent data leakage and facilitate reproducible deployments:

```
Raw Input Data
      │
      ├── Drop 'CustomerID'
      ├── Type Cast 'TotalCharges' (coerce, fillna 0)
      ├── Map 'PaperlessBilling' (Yes:1, No:0)
      │
      ├── Split: Features (X) & Target (y)
      │
      ├── ColumnTransformer
      │     ├── Numerical Features ────> StandardScaler()
      │     └── Categorical Features ──> OneHotEncoder(drop='first', handle_unknown='ignore')
      │
      └── Final Output: X_final (Processed 2D array / DataFrame)
```

### 6.1 Processed Feature Matrix Columns (9 Total Features)
1. `Tenure` (Standardized)
2. `MonthlyCharges` (Standardized)
3. `TotalCharges` (Standardized)
4. `PaperlessBilling` (Standardized)
5. `SeniorCitizen` (Standardized)
6. `Contract_One year` (Binary One-Hot)
7. `Contract_Two year` (Binary One-Hot)
8. `PaymentMethod_Credit Card` (Binary One-Hot)
9. `PaymentMethod_Electronic Check` (Binary One-Hot)

---

## 7. Train/Test Data Partitioning

* **Strategy:** Stratified Train/Test Split (`train_test_split`).
* **Parameters:**
  * `test_size`: 0.20 (20% reserved for validation)
  * `random_state`: 42 (ensures deterministic reproducibility)
  * `stratify`: `y_final` (preserves churn-to-non-churn class ratios across splits)
* **Resulting Partitions:**
  * **$X_{\text{train}}$ Shape:** $(400, 9)$
  * **$X_{\text{test}}$ Shape:** $(100, 9)$
  * **$y_{\text{train}}$ Shape:** $(400,)$
  * **$y_{\text{test}}$ Shape:** $(100,)$

---

## 8. Recommendations & Best Practices for Next Phase

1. **Avoid Data Leakage in Pipelines:**
   * In the standalone function, `.fit_transform()` was run across the full dataset prior to splitting.
   * *Recommendation:* Apply `pipeline.fit_transform(X_train)` on the training set only, followed by `pipeline.transform(X_test)` on the holdout partition to prevent test distribution parameters from leaking into scaler statistics ($\mu, \sigma$).
2. **Incorporate Engineered Features into Pipeline:**
   * The engineered interaction features (`AvgChargePerTenure`, `IsLongTermCustomer`, etc.) can be wrapped into a custom `FunctionTransformer` or `BaseEstimator` class and placed at the beginning of the `Pipeline`.
3. **Class Imbalance Assessment:**
   * Check the positive class balance for `Churn`. If significant skew exists, consider threshold-tuning, class weighting (`class_weight='balanced'`), or resampling methods (SMOTE) on the training fold.