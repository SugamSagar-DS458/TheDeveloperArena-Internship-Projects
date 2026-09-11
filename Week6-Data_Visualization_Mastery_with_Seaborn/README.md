# 📊 Data Visualization Mastery with Seaborn

**Week 6 Project — The Developer Arena Internship (Data Science Track)**

A hands-on exploratory data analysis (EDA) and visualization project built on a retail sales dataset. This project demonstrates the use of **Seaborn**, **Matplotlib**, and **Plotly** to uncover sales trends, regional performance, product-level insights, and customer purchase behavior.

---

## 📌 Project Overview

This notebook was developed as part of **Week 6** of The Developer Arena Internship, focused on mastering data visualization techniques in Python. The goal was to take a raw sales dataset and transform it into clear, actionable visual insights using a combination of static (Seaborn/Matplotlib) and interactive (Plotly) charting libraries.

## 🎯 Objectives

- Clean and preprocess raw sales data (date parsing, feature extraction)
- Analyze sales trends over time
- Compare sales performance across regions and products
- Study the relationship between customer purchase quantity and revenue
- Identify correlations between numerical sales metrics
- Present findings through polished, publication-ready visualizations

## 🗂️ Dataset

The dataset (`sales_data.csv`) contains transactional retail sales records with the following key fields:

| Column | Description |
|---|---|
| `Date` | Date of the transaction |
| `Region` | Sales region |
| `Product` | Product name/category |
| `Quantity` | Units sold |
| `Price` | Unit price |
| `Total_Sales` | Total revenue for the transaction |
| `Customer_ID` | Unique customer identifier |

> 📁 Place `sales_data.csv` in the project directory (or update the file path in the notebook) before running.

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** — data manipulation & preprocessing
- **Seaborn** — statistical data visualization
- **Matplotlib** — plot customization and rendering
- **Plotly Express / Graph Objects** — interactive visualizations
- **Jupyter Notebook** — development environment

## 📈 Visualizations & Analysis

| # | Visualization | Library | Insight |
|---|---|---|---|
| 1 | Daily Sales Trend (line chart with range slider) | Plotly | Tracks revenue fluctuations over time |
| 2 | Total Sales by Region (bar chart) | Plotly | Identifies top and underperforming regions |
| 3 | Sales Distribution per Region (boxplot) | Seaborn | Highlights variance and outliers in regional sales |
| 4 | Total Sales by Product (bar chart) | Plotly | Ranks products by revenue contribution |
| 5 | Customer Quantity vs. Total Sales (scatter plot) | Seaborn | Reveals high-value customer segments |
| 6 | Correlation Heatmap (Quantity, Price, Total Sales) | Seaborn | Shows relationships between numerical features |
| 7 | Average Sales per Region (bar chart) | Plotly | Compares average transaction value across regions |

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Install dependencies
```bash
pip install pandas seaborn matplotlib plotly jupyter
```

### 3. Run the notebook
```bash
jupyter notebook Week6_Data_Visualization_Mastery_with_Seaborn.ipynb
```

## 🖼️ Screenshots

Sample outputs generated :

### Daily Sales Trend Over Time
![Daily Sales Trend Over Time](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week6-Data_Visualization_Mastery_with_Seaborn/Daily%20Sales%20Trend%20Over%20Time.png)

### Total Sales by Region
![Total Sales by Region](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week6-Data_Visualization_Mastery_with_Seaborn/Total%20Sales%20by%20Region.png)

### Distribution of Total Sales per Region- Box Plot
![Distribution of Total Sales per Region-Box Plot](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week6-Data_Visualization_Mastery_with_Seaborn/Distribution%20of%20Total%20Sales%20per%20Region.png)

### Total Sales by Product
![Total Sales by Product](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week6-Data_Visualization_Mastery_with_Seaborn/Total%20Sales%20by%20Product.png)

### Customer Lifetime Value: Total Quantity vs. Total Sales
![Customer Lifetime Value: Total Quantity vs. Total Sales](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week6-Data_Visualization_Mastery_with_Seaborn/Customer%20Lifetime%20Value%20Total%20Quantity%20vs.%20Total%20Sales.png)

### Correlation Matrix of Numerical Features
![Correlation Matrix of Numerical Features](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week6-Data_Visualization_Mastery_with_Seaborn/Correlation%20Matrix%20of%20Numerical%20Features.png)

### Average Total Sales per Region
![Average Total Sales per Region](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week6-Data_Visualization_Mastery_with_Seaborn/Average%20Total%20Sales%20per%20Region.png)

### Dashboard Demo
![Dashboard_Demo](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week6-Data_Visualization_Mastery_with_Seaborn/dashboard_demo.gif)

## 🔍 Key Insights

- Sales trends show clear day-to-day fluctuations, useful for spotting seasonal peaks.
- Certain regions and products consistently outperform others in total revenue.
- A positive correlation exists between quantity sold and total sales, as expected, while price shows a more nuanced relationship with revenue.
- A small segment of high-value customers contributes disproportionately to total sales — useful for targeted marketing.

## 📚 What I Learned

- Building both static and interactive visualizations for the same dataset and knowing when to use each
- Data preprocessing techniques like datetime conversion and feature extraction (`Month`)
- Using `groupby()` and aggregation functions to derive business metrics
- Customizing Seaborn/Matplotlib plots (titles, labels, palettes, grid styling) for readability
- Creating interactive Plotly charts with range sliders and hover tooltips

## 👤 Author

**Sugam Sagar**
Data Science Intern — The Developer Arena Internship
🔗 [LinkedIn](https://www.linkedin.com/in/sugamsagar-ai) | 💻 [GitHub](https://github.com/SugamSagar-DS458)

## 📄 License

This project was created for educational purposes as part of The Developer Arena Internship program.

---
⭐ If you found this project helpful, consider giving it a star!
