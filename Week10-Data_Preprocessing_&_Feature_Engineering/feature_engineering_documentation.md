# Customer Churn Prediction: Feature Engineering Documentation

## 1. Overview & Purpose

Feature engineering translates raw transactional and demographic variables into informative signals that help machine learning algorithms isolate customer churn behaviors. 

In customer churn modeling, churn risk is rarely dictated by isolated static values (such as tenure or monthly cost in isolation); rather, it is driven by **relative pricing pacing**, **tenure milestones**, and **cost-to-duration ratios**.

This document details the definition, mathematical formulation, edge-case mitigation, and business rationale for all engineered features developed in the project.

---

## 2. Summary of Raw Features Used as Base Inputs

| Feature | Data Type | Description |
| :--- | :--- | :--- |
| `Tenure` | Integer (`int64`) | Total number of months the customer has stayed with the company. |
| `MonthlyCharges` | Float / Integer (`int64`) | The amount charged to the customer on a monthly recurring basis. |
| `TotalCharges` | Float (`float64`) | Total cumulative amount billed to the customer across their entire lifecycle. |

---

## 3. Engineered Features Specification

### 3.1 `AvgChargePerTenure` (Average Charge Per Tenure Month)

* **Definition:** Estimates the empirical average monthly revenue realized per unit of tenure.
* **Mathematical Formula:**

  $$
  \text{AvgChargePerTenure} = \frac{\text{TotalCharges}}{\text{Tenure}}
  $$

* **Implementation Logic:**
  ```python
  df_engineered['AvgChargePerTenure'] = df_engineered['TotalCharges'] / df_engineered['Tenure']
  df_engineered['AvgChargePerTenure'] = (
      df_engineered['AvgChargePerTenure']
      .replace([np.inf, -np.inf], np.nan)
      .fillna(df_engineered['MonthlyCharges'])
  )
  ```
* **Edge-Case Handling:**
  * **Division by Zero:** When $\text{Tenure} = 0$ (brand-new accounts), normal division yields $\infty$. These values are converted to `NaN` and imputed with current `MonthlyCharges` as the best single-month baseline estimate.
* **Business & Machine Learning Rationale:**
  * Discrepancies between `AvgChargePerTenure` and current `MonthlyCharges` signal recent pricing modifications, plan upgrades, discount roll-offs, or add-on service attachments. A sharp surge in billing relative to historical averages is a frequent churn catalyst.

---

### 3.2 `IsLongTermCustomer` (Long-Term Retention Flag)

* **Definition:** A binary indicator distinguishing long-tenured customers from early-tenure cohorts using a 24-month (2-year contract cycle) threshold.
* **Mathematical Formula:**

  $$
  \text{IsLongTermCustomer} = 
  \begin{cases} 
  1, & \text{if } \text{Tenure} > 24 \\
  0, & \text{otherwise}
  \end{cases}
  $$

* **Implementation Logic:**
  ```python
  df_engineered['IsLongTermCustomer'] = (df_engineered['Tenure'] > 24).astype(int)
  ```
* **Edge-Case Handling:**
  * Deterministic boolean evaluation; no nulls or infinite values generated.
* **Business & Machine Learning Rationale:**
  * Empirical hazard rates in telecommunications follow a bathtub curve: churn probability is elevated during months 1–12 and contract renewal boundaries (month 12 and month 24). Customers persisting beyond 24 months demonstrate established platform adoption and lower natural baseline churn.

---

### 3.3 `MonthlyChargeToTotalChargeRatio` (Billing Velocity Ratio)

* **Definition:** Quantifies the proportion of cumulative historical spending represented by the current monthly billing statement.
* **Mathematical Formula:**

  $$
  \text{MonthlyChargeToTotalChargeRatio} = \frac{\text{MonthlyCharges}}{\text{TotalCharges}}
  $$

* **Implementation Logic:**
  ```python
  df_engineered['MonthlyChargeToTotalChargeRatio'] = df_engineered['MonthlyCharges'] / df_engineered['TotalCharges']
  df_engineered['MonthlyChargeToTotalChargeRatio'] = (
      df_engineered['MonthlyChargeToTotalChargeRatio']
      .replace([np.inf, -np.inf], np.nan)
      .fillna(0)
  )
  ```
* **Edge-Case Handling:**
  * When $\text{TotalCharges} = 0$, division generates $\infty$. Handled by substituting $\infty$ with `0`.
* **Business & Machine Learning Rationale:**
  * High ratio values approaching $1.0$ indicate nascent accounts whose recent bill constitutes most of their lifetime monetary exposure. Such users are sensitive to price perception shock. Conversely, tiny fractions ($\to 0$) denote long-accumulated loyalty where individual invoice variations have minor psychological churn impact.

---

### 3.4 `TenureToMonthlyChargeRatio` (Loyalty Return on Expenditure)

* **Definition:** Assesses months of accumulated relationship relative to monthly cost rate.
* **Mathematical Formula:**

  $$
  \text{TenureToMonthlyChargeRatio} = \frac{\text{Tenure}}{\text{MonthlyCharges}}
  $$

* **Implementation Logic:**
  ```python
  df_engineered['TenureToMonthlyChargeRatio'] = df_engineered['Tenure'] / df_engineered['MonthlyCharges']
  df_engineered['TenureToMonthlyChargeRatio'] = (
      df_engineered['TenureToMonthlyChargeRatio']
      .replace([np.inf, -np.inf], np.nan)
      .fillna(0)
  )
  ```
* **Edge-Case Handling:**
  * When $\text{MonthlyCharges} = 0$ (e.g., promotional free-tier accounts), division-by-zero results are replaced with `0`.
* **Business & Machine Learning Rationale:**
  * Represents tenure seniority normalized by plan cost tier. High values characterize customers who have sustained relationships on low-cost plans, while low values highlight accounts paying high recurring charges without long-term commitment history.

---

### 3.5 `IsHighValueCustomer` (Lifetime Revenue Partition Flag)

* **Definition:** A non-parametric binary indicator tagging customers in the top $50^{\text{th}}$ percentile of overall revenue generation.
* **Mathematical Formula:**

  $$
  \text{IsHighValueCustomer} = 
  \begin{cases} 
  1, & \text{if } \text{TotalCharges} > \operatorname{Median}(\text{TotalCharges}) \\
  0, & \text{otherwise}
  \end{cases}
  $$

* **Implementation Logic:**
  ```python
  df_engineered['IsHighValueCustomer'] = (
      df_engineered['TotalCharges'] > df_engineered['TotalCharges'].median()
  ).astype(int)
  ```
* **Edge-Case Handling:**
  * Robust against right-skewed revenue distributions by selecting median rather than arithmetic mean.
* **Business & Machine Learning Rationale:**
  * Retaining high-lifetime-value customers has a disproportionately positive impact on customer lifetime value (CLV) retention programs. This segmentation aids downstream business actions and tree-based decision thresholding.

---

## 4. Comprehensive Feature Matrix Summary

| Feature Name | Type | Derived From | Imputation Rule | Downstream Scaling Needed |
| :--- | :--- | :--- | :--- | :--- |
| `AvgChargePerTenure` | Continuous (Float) | `TotalCharges`, `Tenure` | `MonthlyCharges` for $\text{Tenure}=0$ | Yes (`StandardScaler`) |
| `IsLongTermCustomer` | Binary (`0`/`1`) | `Tenure` | N/A | No (binary flag) |
| `MonthlyChargeToTotalChargeRatio` | Continuous (Float) | `MonthlyCharges`, `TotalCharges` | `0` for $\text{TotalCharges}=0$ | Yes (`StandardScaler`) |
| `TenureToMonthlyChargeRatio` | Continuous (Float) | `Tenure`, `MonthlyCharges` | `0` for $\text{MonthlyCharges}=0$ | Yes (`StandardScaler`) |
| `IsHighValueCustomer` | Binary (`0`/`1`) | `TotalCharges` | N/A | No (binary flag) |

---

## 5. Integration into Production Pipelines

To deploy these transformations cleanly in `scikit-learn` without data leakage, encapsulate the engineering logic in a custom transformer class or `FunctionTransformer`:

```python
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

class FeatureEngineeringTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.median_total_charges_ = None

    def fit(self, X, y=None):
        # Learn distribution statistics strictly from the training split
        self.median_total_charges_ = X['TotalCharges'].median()
        return self

    def transform(self, X):
        X_out = X.copy()
        
        # 1. AvgChargePerTenure
        avg_charge = X_out['TotalCharges'] / X_out['Tenure']
        X_out['AvgChargePerTenure'] = avg_charge.replace([np.inf, -np.inf], np.nan).fillna(X_out['MonthlyCharges'])
        
        # 2. IsLongTermCustomer
        X_out['IsLongTermCustomer'] = (X_out['Tenure'] > 24).astype(int)
        
        # 3. MonthlyChargeToTotalChargeRatio
        m_to_t = X_out['MonthlyCharges'] / X_out['TotalCharges']
        X_out['MonthlyChargeToTotalChargeRatio'] = m_to_t.replace([np.inf, -np.inf], np.nan).fillna(0)
        
        # 4. TenureToMonthlyChargeRatio
        t_to_m = X_out['Tenure'] / X_out['MonthlyCharges']
        X_out['TenureToMonthlyChargeRatio'] = t_to_m.replace([np.inf, -np.inf], np.nan).fillna(0)
        
        # 5. IsHighValueCustomer (uses training median)
        X_out['IsHighValueCustomer'] = (X_out['TotalCharges'] > self.median_total_charges_).astype(int)
        
        return X_out
```

### Key Deployment Consideration:
* Computing statistical thresholds (such as `TotalCharges.median()`) directly on the entire dataset leads to data leakage. Fitting statistics strictly on the training set ensures the evaluation on test or production data remains unbiased.