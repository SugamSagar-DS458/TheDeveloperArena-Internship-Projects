# Advanced Data Manipulation Using Pandas

**The Developer Arena Internship — Week 5 Project**

A data analytics project focused on advanced Pandas techniques — merging datasets, reshaping data with pivot tables, aggregating business metrics, and visualizing insights from customer and sales data.

---

## 📌 Project Overview

This project analyzes two related datasets — **customer churn data** and **sales transaction data** — to uncover business insights such as revenue trends, top-performing products, high-value customers, and the relationship between contract type and customer churn.

The notebook demonstrates practical, real-world Pandas skills including:

- Merging and reshaping data from multiple sources
- Cleaning and standardizing key fields for joins
- Aggregation with `groupby()` and `pivot_table()`
- Deriving business KPIs (revenue, average order value, top customers)
- Data visualization with Matplotlib and Seaborn

## 🗂️ Datasets

| Dataset | Description |
|---|---|
| `customer_churn.csv` | Customer-level data including contract type, monthly charges, and churn status |
| `sales_data.csv` | Transaction-level sales data including product, region, date, and revenue |

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** — data manipulation and analysis
- **Matplotlib** & **Seaborn** — data visualization
- **Jupyter Notebook** — development environment

## 📁 Project Structure

```
Week5-Advance_Data_Manipulation_Using_Panda/
│
├── Week5-Advance_Data_Manipulation_Using_Panda.ipynb   # Main analysis notebook
├── customer_churn.csv                                  # Customer churn dataset
├── sales_data.csv                                       # Sales transaction dataset
├── assets/                                              # Output charts (screenshots)
└── README.md                                            # Project documentation
```

## 🔍 Workflow

### 1. Data Loading & Inspection
Both CSV files are loaded into Pandas DataFrames, and their structure is inspected using `.info()` and `.head()`.

```python
import pandas as pd

customer_churn_df = pd.read_csv('customer_churn.csv')
sales_df = pd.read_csv('sales_data.csv')

customer_churn_df.info()
sales_df.info()
```

### 2. Data Cleaning & Merging
The `CustomerID` columns are standardized across both datasets, and the datasets are merged into a single DataFrame for unified analysis. The `Date` column is also converted to a proper datetime type so `Month` and `Year` can be extracted.

```python
# Standardize CustomerID format for a proper merge
sales_df = sales_df.rename(columns={'Customer_ID': 'CustomerID'})
customer_churn_df['CustomerID'] = customer_churn_df['CustomerID'].apply(
    lambda x: x.replace('C', 'CUST')
)

# Merge datasets
merged_df = pd.merge(sales_df, customer_churn_df, on='CustomerID', how='left')

# Extract date parts
merged_df['Date'] = pd.to_datetime(merged_df['Date'])
merged_df['Month'] = merged_df['Date'].dt.month
merged_df['Year'] = merged_df['Date'].dt.year
```

### 3. Aggregation & Analysis
Using `groupby()` and `pivot_table()`, the notebook computes:

- Total sales by year and month
- Total sales by product
- Top 10 customers by total sales
- Total sales by product and region (pivot table)
- Average monthly charges and churn rate by contract type (pivot table)

```python
# Total Sales by Product
sales_by_product = merged_df.groupby('Product')['Total_Sales'].sum().reset_index()

# Pivot table: Total Sales by Product and Region
sales_region_product_pivot = merged_df.pivot_table(
    values='Total_Sales',
    index='Product',
    columns='Region',
    aggfunc='sum'
).fillna(0)

# Pivot table: Avg Monthly Charges & Churn Rate by Contract Type
churn_contract_pivot = customer_churn_df.pivot_table(
    values=['MonthlyCharges', 'Churn'],
    index='Contract',
    aggfunc={'MonthlyCharges': 'mean', 'Churn': 'mean'}
).rename(columns={'Churn': 'Churn Rate'})
```

### 4. Business KPI Summary
Key performance indicators are calculated to summarize overall business performance.

```python
total_revenue = merged_df['Total_Sales'].sum()
total_customers = merged_df['CustomerID'].nunique()
average_order_value = total_revenue / len(merged_df)

top_customer_id = top_customers.iloc[0]['CustomerID']
top_customer_sales = top_customers.iloc[0]['Total_Sales']

print("CUSTOMER SALES ANALYSIS REPORT")
print(f"Total Revenue: ${total_revenue:,.0f}")
print(f"Total Customers: {total_customers:,.0f}")
print(f"Average Order Value: ${average_order_value:,.0f}")
print(f"Top Customer: {top_customer_id} - ${top_customer_sales:,.0f}")
```

### 5. Data Visualization
Seaborn and Matplotlib are used to visualize trends and comparisons across the data.

## 📊 Output Screenshots

**Total Sales Over Time**

![Total Sales Over Time](assets/sales_over_time.png)

**Total Sales by Product**

![Total Sales by Product](assets/sales_by_product.png)

**Top 10 Customers by Total Sales**

![Top 10 Customers](assets/top10_customers.png)

**Total Sales by Product and Region**

![Sales by Product and Region](assets/sales_product_region.png)

**Churn Rate & Average Monthly Charges by Contract Type**

![Churn vs Contract Type](assets/churn_contract.png)

## 💡 Key Insights

- Total sales fluctuated month-to-month, with a peak followed by a sharp decline — indicating potential seasonality or a data gap in the most recent month.
- A clear set of top-performing products and top-spending customers emerged, useful for targeted marketing and retention strategies.
- Customers on **month-to-month contracts** show a noticeably higher churn rate compared to those on longer-term contracts, suggesting that contract length is a strong lever for reducing churn.

## 🚀 How to Run

1. Clone or download this repository.
2. Ensure `customer_churn.csv` and `sales_data.csv` are placed in the same directory as the notebook (update file paths in the first cell if needed).
3. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn jupyter
   ```
4. Launch Jupyter Notebook and run all cells:
   ```bash
   jupyter notebook "Week5-Advance_Data_Manipulation_Using_Panda.ipynb"
   ```

## 🎓 Acknowledgment

This project was completed as part of **Week 5** of **The Developer Arena Internship**, under the module *Advanced Data Manipulation Using Pandas*.

## 👤 Author

Sugam Sagar — Data Science Intern, The Developer Arena Internship
