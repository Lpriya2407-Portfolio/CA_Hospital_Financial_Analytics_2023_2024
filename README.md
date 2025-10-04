# 📊 CA Hospital Financial Analytics (2023–2024)

Quickly analyze and compare top and bottom hospitals in California (2023–2024) by net profit margin (%) using Python and Power BI to reveal key operational and financial insights.


## Project Summary  
End-to-end **ETL, EDA, and KPI analysis** of the *2023–2024 Fiscal Year Hospital Annual Financial Data* (extracted September 2025).  
The dataset originally contained **450+ hospitals** and **10,000+ financial/operational columns**. After cleaning and transformation,  
the final analysis focused on **75 hospitals**, with deeper insights on **Top 5** and **Bottom 5 hospitals** by **Net Profit Margin**.  

This project combines **Python-based analysis** and an **interactive Power BI dashboard** to explore both **operational KPIs** and **financial performance**.  

---

## 🔑 Critical Findings

### Cost Efficiency Issues
 ➤ Cost per patient day varies dramatically: **$785 (best) to $2,444 (worst)**
 ➤ Unprofitable hospitals have **2–3x higher costs per patient day**
 ➤ Average cost per discharge: **$14,582**

### Revenue Collection Problems
 ➤ Unprofitable hospitals show massive **gross-to-net revenue gaps**
 ➤ Example: **Beverly Community** has $365M gross but only $92M net (**75% deduction rate!**)
 ➤ Suggests major **payer mix issues or collection inefficiencies**

### Labor Cost Burden
 ➤ Labor (salaries + benefits) represents **40–60% of total costs**
 ➤ Unprofitable hospitals haven't optimized **staffing ratios**
 ➤ **Contra Costa** has highest absolute labor costs but maintains profitability through volume

### Volume & Scale Matter
 ➤ High outpatient volume = better margins (**Contra Costa: 557K visits, 15.8% margin**)
 ➤ Low-volume hospitals struggle (**Coalinga: 11K visits, -138% margin**)
 ➤ **Economies of scale** are critical for profitability

 ---


## 🛠️ Tools & Technologies Utilised
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

---

## 🔹 Key EDA Focus  
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

---

## 📂 Repository Structure

Healthcare_Analytics_Project/

## 📂 Repository Structure

Healthcare_Analytics_Portfolio/

├─ [Dashboard](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/tree/main/Healthcare_Analytics_Project/Dashboard)

├─ [Data](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/tree/main/Healthcare_Analytics_Project/Data)

├─ [Deliverables](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/tree/main/Healthcare_Analytics_Project/Deliverables)

├─ [Images](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/tree/main/Healthcare_Analytics_Project/Images)

├─ [Insights](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/tree/main/Healthcare_Analytics_Project/Insights)

├─ [Python_Code](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/tree/main/Healthcare_Analytics_Project/Python_Code) 

└─ [Summary](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/tree/main/Healthcare_Analytics_Project/Summary)

---

## 🖼️ Sample Visuals

![EDA Plot](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/blob/main/Healthcare_Analytics_Project/Images/eda_plots.png)
![Top vs Bottom 5](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/blob/main/Healthcare_Analytics_Project/Images/top_bottom_hospitals.png)
![Dashboard Preview](https://github.com/Lpriya2407-Portfolio/CA_Hospital_Financial_Analytics_2023_2024/blob/main/Healthcare_Analytics_Project/Images/dashboard_preview.png)

---


## 📌 Next Steps
- Extend to **multi-year data** for trend analysis  
- Apply **predictive models (Regression/Forecasting)** if more data is available  
- Expand dashboard with **Key Influencer visuals** in Power BI  




