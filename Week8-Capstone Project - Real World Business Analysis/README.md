# E-Commerce Customer Churn Analytics & Lifecycle Optimization Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Internship](https://img.shields.io/badge/Organization-The%20Developers%20Arena-1A365D.svg)](https://thedevelopersarena.com)

> **Role:** Data Science Intern  
> **Track:** Business Analytics & Applied Machine Learning  
> **Domain:** E-Commerce / Customer Lifecycle & Retention  

---

## 📌 Executive Overview
Customer retention in digital commerce represents a high-leverage growth engine compared to rising Customer Acquisition Costs (CAC). This project executes an end-to-end data science investigation analyzing **1,200 customer transaction accounts across 20 behavioral, service, and transactional features**. 

Through a combination of **Econometric Regression Inferences**, **Random Forest Supervised Classification**, and **K-Means Behavioral Clustering**, we diagnose attrition catalysts and deploy an automated early-warning framework projecting an **18% net reduction in churn** and preserving an estimated **$210,000 in at-risk annual Gross Merchandise Value (GMV)**.

---

## 🛠️ Key Analytical Findings
1. **The Support Complaint Multiplier ($p < 0.001$):** Submitting an unresolved customer complaint multiplies the odds of churning by **5.05x**. Even top-tier satisfied customers (Score 5) experience a churn surge from **8.8% to 45.8%** upon logging a complaint.
2. **The 90-Day Drop-Off Cliff:** Accounts in their first 0–3 months of tenure churn at **3.8x** the baseline rate of accounts active beyond month 6.
3. **The 14-Day Inactivity Boundary:** Beyond 14 consecutive dormant days without an order, churn rates spike to **62.8%**, identifying **Day 10** as the critical automated re-engagement trigger.
4. **Loyalty Protection:** Accounts utilizing cashback tiers (> $200) exhibit a **42% lower churn rate**, proving price elasticity directly governs repeat orders.

---

## 📊 Project Structure
```text
├── README.md                      # Comprehensive project documentation & business translation
├── requirements.txt               # Complete Python runtime dependencies
├── capstone_analysis.ipynb        # Master end-to-end executable pipeline
│
├── data/                          # Dataset directory
│   ├── raw_data.csv               # Raw Kaggle-standard transaction logs (1,200 rows, 20 features)
│   └── cleaned_data.csv           # Imputed, Winsorized, and preprocessed dataset
│
├── reports/                       # Formal stakeholder deliverables
│   ├── executive_summary.pdf      # 1-Page executive brief for senior leadership
│   ├── technical_report.pdf       # Comprehensive 5+ page academic & engineering report
│   ├── portfolio_page.html        # Interactive HTML showcase page
│   └── portfolio_page.md          # Markdown portfolio summary
│
└── presentation/                  # Slide deck deliverable
    └── business_presentation.pptx # 12-slide executive presentation with visuals & roadmap
```

---

## 🔬 Methodology & Model Performance

| Technique | Implementation | Core Output / Metric | Business Utility |
| :--- | :--- | :--- | :--- |
| **Econometric Logistic Regression** | `statsmodels.Logit` | Odds Ratio = 5.05 for Complaints ($p < 0.001$) | Quantified causal root causes of account drop-off |
| **Supervised Ensemble Classifier** | `RandomForestClassifier` | **89.3% Accuracy**, **0.76–0.91 ROC-AUC** | Generates automated daily risk scores per account |
| **Unsupervised Audience Clustering** | `KMeans(n_clusters=3)` | 3 Distinct Behavioral Cohorts | Informs personalized CRM and coupon allocations |

### Cluster Archetypes:
* **Cluster 0 — Core Loyalists (4.2% Churn):** High tenure (> 18 mos), frequent orders (6.8 avg), minimal complaints. *Action: VIP perks & exclusive previews.*
* **Cluster 1 — Dormant At-Risk (62.8% Churn):** Low tenure (2.1 mos), high dormancy (16.4 days). *Action: High-urgency win-back incentives.*
* **Cluster 2 — Price Sensitive (19.5% Churn):** Moderate frequency, responsive to discounts. *Action: Triggered cashback vouchers.*

---

## 🚀 Quickstart & Reproduction

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the Pipeline
Open Jupyter Notebook and run `capstone_analysis.ipynb`:
```bash
jupyter notebook capstone_analysis.ipynb
```

---

## 📅 60-Day Business Implementation Roadmap
* **Weeks 1–2 (Integration):** Deploy model script to production SQL warehouse; run daily batch scoring.
* **Weeks 3–4 (Service SLA):** Re-route support tickets from high-risk accounts to a **2-hour priority resolution SLA**.
* **Weeks 5–6 (Lifecycle Automation):** Configure CRM to trigger category win-back coupons on **Day 10 of inactivity**.
* **Weeks 7–8 (Controlled Trial):** Run 10% holdout A/B validation to measure net preserved Gross Merchandise Value (GMV).

---

## 👤 Author
* **Role:** Data Science Intern
* **Organization:** The Developers Arena
* **Project Repository:** [GitHub Link](https://github.com/<your-username>/<your-repo-name>)
