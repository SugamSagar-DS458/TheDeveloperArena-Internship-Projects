# 📊 Statistical Analysis of Sales Data

> A data science project completed as part of **The Developer Arena Internship** (Week 7), focused on applying core statistical inference and regression techniques to real-world sales data using Python.

---

## 📌 Overview

This project performs an end-to-end statistical analysis on a retail sales dataset. It covers exploratory data analysis, hypothesis testing, correlation analysis, confidence interval estimation, and multiple linear regression — culminating in diagnostic visualizations of the regression model.

The goal is to determine whether factors such as **Region** and **Product Type** have a statistically significant relationship with **Total Sales**, and to model how **Quantity** and **Price** influence sales performance.

---

## 🧠 Key Analyses Performed

| # | Analysis | Purpose |
|---|----------|---------|
| 1 | **Exploratory Data Analysis** | Inspect structure, data types, and summary statistics of the dataset |
| 2 | **One-Way ANOVA** | Test whether `Total_Sales` differs significantly across `Region` |
| 3 | **Independent Samples T-Test** | Compare `Total_Sales` between two product categories (Phone vs. Laptop) |
| 4 | **Chi-Square Test of Independence** | Test the relationship between `Product` and `Region` |
| 5 | **Correlation Analysis** | Examine relationships between `Quantity`, `Price`, and `Total_Sales` |
| 6 | **Confidence Interval Estimation** | Estimate the 95% CI for mean `Total_Sales` |
| 7 | **Multiple Linear Regression (OLS)** | Model `Total_Sales` as a function of `Quantity` and `Price` |
| 8 | **Regression Diagnostics** | Residual plots and regression line visualizations to assess model fit |

---

## 🛠️ Tech Stack

- **Python 3**
- **pandas** – data manipulation
- **scipy.stats** – hypothesis testing (ANOVA, t-test, chi-square)
- **statsmodels** – OLS regression modeling
- **matplotlib** & **seaborn** – data visualization
- **Jupyter Notebook** – interactive analysis environment

---

## 📁 Project Structure

```
statistical-analysis-sales/
│
├── statistical_analysis.ipynb   # Main analysis notebook
├── sales_data.csv               # Dataset (Region, Product, Quantity, Price, Total_Sales)
├── screenshots/                 # Output visualizations (see below)
└── README.md                    # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/statistical-analysis-sales.git
   cd statistical-analysis-sales
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install pandas scipy statsmodels matplotlib seaborn jupyter
   ```

4. **Run the notebook**
   ```bash
   jupyter notebook statistical_analysis.ipynb
   ```

---

## ▶️ Usage

Update the dataset path in the first cell to point to your local copy of `sales_data.csv`, then run all cells sequentially:

```python
sales_df = pd.read_csv("sales_data.csv")
display(sales_df.head())
```

Each hypothesis test prints its statistic, p-value, and a plain-language conclusion (e.g., significant vs. not significant at α = 0.05), and the regression section prints the full OLS model summary.

---

## 🖼️ Screenshots

### Residual Plot
![Residual Plot](screenshots/residual_plot.png)

### Total Sales vs. Quantity Regression
![Regression Plot](screenshots/regression_line_plot.png)

---

## 📈 Sample Findings

- **ANOVA** revealed whether `Total_Sales` varies significantly across regions.
- **T-Test** compared sales performance between Phones and Laptops.
- **Chi-Square Test** assessed whether product type and region are independent.
- **Regression Model** quantified how `Quantity` and `Price` jointly predict `Total_Sales`, with residual plots used to validate model assumptions (linearity, homoscedasticity).

*(Exact statistics and conclusions are generated at runtime and printed in the notebook output.)*

---

## 🎓 Acknowledgment

This project was developed as part of **The Developer Arena Internship Program**, under the Data Science track, to build hands-on experience with statistical hypothesis testing and regression analysis in Python.

---

## 📄 License

This project is intended for educational and portfolio purposes.
