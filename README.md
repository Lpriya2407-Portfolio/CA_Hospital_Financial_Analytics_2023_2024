# 📊 CA Hospital Financial Analytics (2023–2024)

Quickly analyze and compare top and bottom hospitals in California (2023–2024) using Python and Power BI to reveal key operational and financial insights.


## Project Summary  
End-to-end **ETL, EDA, and KPI analysis** of the *2023–2024 Fiscal Year Hospital Annual Financial Data* (extracted September 2025).  
The dataset originally contained **450+ hospitals** and **10,000+ financial/operational columns**. After cleaning and transformation,  
the final analysis focused on **75 hospitals**, with deeper insights on **Top 5** and **Bottom 5 hospitals** by **Net Profit Margin**.  

This project combines **Python-based analysis** and an **interactive Power BI dashboard** to explore both **operational KPIs** and **financial performance**.  

---

## 🛠️ Tools & Technologies
- **Python** → Pandas, NumPy, Matplotlib, Seaborn, Plotly, Bokeh (data cleaning, EDA, visualization)  
- **Power BI** → Data modeling, KPI dashboards, interactive visualizations  
- **Excel / Power Query** → Initial data cleaning, transformation, and null handling  
- **Git & GitHub** → Version control and project repository management

---

## 🔄 ETL Process
- **Source:** Excel file with 450+ rows × 10,000+ columns (Revenue, Expenses, Costs, Staff, Beds, Profits, etc.)  
- **Transformations:**  
  - Removed null-heavy rows & columns in Excel/Power Query  
  - Reduced dataset to **75 hospitals** with complete data  
- **Load:** Extracted cleaned file into Python (Pandas DataFrame)  

---

## 📂 Data
The dataset included in this repository is the **cleaned version** used for analysis, containing 75 hospitals and relevant financial & operational columns.  
The **original dataset** had 450+ hospitals and 10,000+ columns and was cleaned to remove null rows/columns and focus on actionable insights.

---

## 🔍 Exploratory Data Analysis (EDA)
Performed in **Python (PyCharm)** using:  
- **NumPy & Pandas** → Data cleaning, calculations, aggregations  
- **Matplotlib & Seaborn** → Trend charts, distribution plots  
- **Bokeh & Plotly** → Interactive visualizations (treemaps, hover insights)  

### Key EDA Focus  
- Net Profit Margin across hospitals  
- Top & Bottom 5 hospitals by profitability  
- Operational vs. financial performance correlations  

---

## 📈 KPI Definitions
1. **Occupancy Rate** = `(Inpatient Days ÷ Bed Days) × 100`  
2. **Bed Utilization** = `(Inpatient Days ÷ (Available Beds × 365)) × 100`  
3. **Staff-to-Bed Ratio** = `Total Staff ÷ Staffed Beds`  

---

## 🧾 Analysis Conducted
- **Revenue Analysis:** Revenue, Costs, Net Profit, Profit Margin  
- **Operational Analysis:** Occupancy Rate, Bed Utilization, Staff-to-Bed ratio  
- **Comparative Analysis:** Top 5 vs. Bottom 5 hospitals (financial + operational)  

---

## 📊 Power BI Dashboard
An **interactive dashboard** was developed in **Power BI**, including:  
- **Revenue Page:** Revenue vs. Cost vs. Net Profit visuals  
- **Operations Page:** Occupancy, Staffing, Bed Utilization charts  
- **Comparisons:** Top/Bottom 5 hospitals highlighted  

👉 [View Dashboard (.pbix file)](Dashboard/Healthcare_Dashboard.pbix)  

---

## 📂 Repository Structure

Healthcare_Analytics_Project/
│
├─ Data/ # Cleaned dataset files
│ └─ Cleaned_Data.xlsx

├─ Python_Code/
│ ├─ revenue_analysis.py

│ ├─ operations_analysis.py

│ └─ visualization_scripts.py

├─ Dashboard/
│ └─ Healthcare_Dashboard.pbix

├─ Images/
│ ├─ eda_plots.png

│ ├─ top_bottom_hospitals.png

│ └─ dashboard_preview.png

└─ README.md

---

## 🖼️ Sample Visuals
![EDA Plot](Images/eda_plots.png)  
![Top vs Bottom 5](Images/top_bottom_hospitals.png)  
![Dashboard Preview](Images/dashboard_preview.png)  

---

## ✅ Key Insights
- Significant performance gap between **Top 5 vs Bottom 5 hospitals** in Net Profit Margin  
- Operational KPIs (Occupancy, Bed Utilization, Staff-to-Bed ratio) strongly correlate with financial outcomes  
- Identified under-utilized hospitals with **excess staffing** relative to bed capacity  

---

## 📌 Next Steps
- Extend to **multi-year data** for trend analysis  
- Apply **predictive models (Regression/Forecasting)** if more data is available  
- Expand dashboard with **Key Influencer visuals** in Power BI  




