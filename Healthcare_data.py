import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # 1. Load dataset
df = pd.read_excel("california_dataset.xlsx")
#
# # 2. Check null counts for all columns
# print("Null counts per column:")
# print(df.isnull().sum())
#
#
# # # 4. Drop rows where Net_Revenue or Gross_Revenue are missing
# # df = df.dropna(subset=["Net_Revenue", "Gross_Revenue"])
#
# # 5. Calculate Net Profit Margin (%)
# # df["net_profit_margin"] = (df["Net_Revenue"] / df["Gross_Revenue"]) * 100
#
# # 6. Sort hospitals by Net Profit Margin
# df_sorted= df.sort_values(by="net_profit_margin(%)", ascending=False)
# # 7. Get Top 5 and Bottom 5 hospitals
# top5 = df_sorted.head(5)
# bottom5 = df_sorted.tail(5)
#
# print("\nTop 5 Hospitals by Net Profit Margin:")
# print(top5)
#
# print("\nBottom 5 Hospitals by Net Profit Margin:")
# print(bottom5)
#
# # 8. Save results (optional)
# # with pd.ExcelWriter("california_hospitals_cleaned.xlsx") as writer:
# #     df_sorted.to_excel(writer, sheet_name="All_Hospitals", index=False)
# #     top5.to_excel(writer, sheet_name="Top5", index=False)
# #     bottom5.to_excel(writer, sheet_name="Bottom5", index=False)
#
#
# import matplotlib.pyplot as plt
#
# # Top 5
# top_labels = ['Top 1', 'Top 2', 'Top 3', 'Top 4', 'Top 5']
# bottom_labels = ['Bottom 5', 'Bottom 4', 'Bottom 3', 'Bottom 2', 'Bottom 1']
#
# plt.bar(top_labels, top5['net_profit_margin(%)'], color='green')
# plt.xticks(rotation=45, ha='right')
# plt.ylabel('Net Profit Margin (%)')
# plt.title('Top 5 Hospitals by Net Profit Margin')
# plt.show()
#
# # Bottom 5
# plt.bar(bottom_labels, bottom5['net_profit_margin(%)'], color='red')
# plt.xticks(rotation=45, ha='right')
# plt.ylabel('Net Profit Margin (%)')
# plt.title('Bottom 5 Hospitals by Net Profit Margin')
# plt.grid(axis='y', linestyle='--', alpha=0.7)  # horizontal grid lines only
# plt.show()


# Define bin edges so max value is included
# bin_edges = np.arange(-150, 51 , 25)  # bins: -150,-125,...,50
#
# plt.figure(figsize=(12,6))
#
# # Histogram
# n, bins, patches = plt.hist(df['net_profit_margin(%)'],
#                             bins=bin_edges,
#                             color='skyblue',
#                             edgecolor='black',
#                             align='right',
#                             rwidth=0.9)  # bar width slightly narrower for clarity
#
# # Grid
# plt.grid(axis='y', linestyle='--', alpha=0.7)
#
# # X-axis ticks exactly at bin starts
# plt.xticks(bin_edges)
#
# # Labels
# plt.xlabel("Net Profit Margin (%)")
# plt.ylabel("Number of Hospitals")
# plt.title("Distribution of Net Profit Margin")
#
# # Add counts on top of bars
# for count, patch in zip(n, patches):
#     plt.text(patch.get_x() + patch.get_width()/2, count + 0.5, int(count),
#              ha='center', va='bottom', fontsize=9)
#
# plt.show

# Columns for stacking
hospital_staff_cols = [
    'Active_Medical_Staff_Hospital_Based_Board_Certified_Total',
    'Active_Medical_Staff_Hospital_Based_Board_Eligible_Total',
    'Active_Medical_Staff_Hospital_Based_Other_Total'
]
#
# non_hospital_staff_cols = [
#     'Active_Medical_Staff_Non-Hospital_Based_Board_Certified_Total',
#     'Active_Medical_Staff_Non-Hospital_Based_Board_Eligible_Total',
#     'Active_Medical_Staff_Non-Hospital_Based_Other_Total'
# ]
#
# # Calculate totals for each category
df['Hospital_Based_Total'] = df[hospital_staff_cols].sum(axis=1)
# df['Non_Hospital_Based_Total'] = df[non_hospital_staff_cols].sum(axis=1)
#
# # Select Top 5 and Bottom 5 based on net profit margin
top5 = df.nlargest(5, 'net_profit_margin(%)')
bottom5 = df.nsmallest(5, 'net_profit_margin(%)')
#
combined = pd.concat([top5, bottom5],ignore_index=True)
combined.reset_index(inplace=True,drop=True)

#
custom_labels = ["T1","T2","T3","T4","T5","B1","B2","B3","B4","B5"]

#
x = np.arange(len(custom_labels))
#
#
#
#
# plt.figure(figsize=(14,6))
#
# # Colors for the stacks (same for both top and bottom)
# hospital_color = 'skyblue'
# non_hospital_color = 'lightgreen'
#
# # Plot Top 5
# plt.bar(x[:5], combined['Hospital_Based_Total'].iloc[:5], label='Hospital-Based Staff', color=hospital_color)
# plt.bar(x[:5], combined['Non_Hospital_Based_Total'].iloc[:5],
#         bottom=combined['Hospital_Based_Total'].iloc[:5], label='Non-Hospital-Based Staff', color=non_hospital_color)
#
# # Plot Bottom 5 (same colors, no extra legend)
# plt.bar(x[5:], combined['Hospital_Based_Total'].iloc[5:], color=hospital_color)
# plt.bar(x[5:], combined['Non_Hospital_Based_Total'].iloc[5:],
#         bottom=combined['Hospital_Based_Total'].iloc[5:], color=non_hospital_color)
#
# # Counts on top of each bar
# for i in range(len(x)):
#     total = combined['Hospital_Based_Total'].iloc[i] + combined['Non_Hospital_Based_Total'].iloc[i]
#     plt.text(x[i], total + 0.5, str(int(total)), ha='center', va='bottom', fontsize=10)
#
# # Custom x labels
# plt.xticks(x, custom_labels, rotation=45, ha='right')
# plt.ylabel('Total Staff')
# plt.title('Total Staff: Top & Bottom 5 Hospitals by Net Profit Margin')
# plt.legend()  # only shows Hospital-Based / Non-Hospital-Based
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()

# # Calculate ratios per hospital-based staff
combined['Patient_Days_per_Staff'] = combined['Patient_(Census)_Days_Total_Total'] / combined['Hospital_Based_Total']
combined['Outpatients_per_Staff'] = combined['Outpatient_Visits_Total_Total'] / combined['Hospital_Based_Total']
combined['Discharges_per_Staff'] = combined['Discharges_Total'] / combined['Hospital_Based_Total']

# X-axis positions
n = len(custom_labels)
x = np.arange(n)
width = 0.25  # width of each bar

plt.figure(figsize=(14,6))

# Plot grouped bars
plt.bar(x - width, combined['Patient_Days_per_Staff'], width=width, label='Patient Days per Staff', color='orange')
plt.bar(x, combined['Discharges_per_Staff'], width=width, label='Discharges per Staff', color='green')
plt.bar(x + width, combined['Outpatients_per_Staff'], width=width, label='Outpatients per Staff', color='skyblue')

# Optional: add values on top
for i in range(n):
    plt.text(x[i] - width, combined['Patient_Days_per_Staff'].iloc[i]+0.05, f"{combined['Patient_Days_per_Staff'].iloc[i]:.1f}", ha='center', va='bottom', fontsize=9)
    plt.text(x[i], combined['Discharges_per_Staff'].iloc[i]+0.05, f"{combined['Discharges_per_Staff'].iloc[i]:.1f}", ha='center', va='bottom', fontsize=9)
    plt.text(x[i] + width, combined['Outpatients_per_Staff'].iloc[i]+0.05, f"{combined['Outpatients_per_Staff'].iloc[i]:.1f}", ha='center', va='bottom', fontsize=9)

# Custom x labels
plt.xticks(x, custom_labels, rotation=45, ha='right')
plt.ylabel('Ratio per Hospital-Based Staff')
plt.title('Patient Days, Discharges, and Outpatients per Staff: Top & Bottom 5 Hospitals', pad=20)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# import pandas as pd
# import seaborn as sns
# from matplotlib.lines import Line2D
#
# # --- Calculate ALOS ---
# df["ALOS"] = df["Patient_(Census)_Days_Total_Total"] / df["Discharges_Total"]
#
# # --- Sort by Net Profit Margin ---
# df_sorted = df.sort_values("net_profit_margin(%)")
#
# # --- Pick Top 5 and Bottom 5 ---
# top5_hosp = df_sorted.tail(5).reset_index(drop=True)
# bottom5_hosp = df_sorted.head(5).reset_index(drop=True)
#
#
# # --- Marker colors ---
# top_colors = sns.color_palette("Greens", n_colors=5)
# bottom_colors = sns.color_palette("Reds", n_colors=5)
#
# plt.figure(figsize=(12,6))
#
# # --- Plot Top 5: line fixed, markers colored ---
# plt.plot(top5_hosp["ALOS"], top5_hosp["net_profit_margin(%)"], color="green", linestyle="-")
# for i in range(len(top5_hosp)):
#     plt.scatter(top5_hosp["ALOS"].iloc[i], top5_hosp["net_profit_margin(%)"].iloc[i],
#                 s=top5_hosp["Net_Patient_Revenue_Total"].iloc[i]/1e6,
#                 color=top_colors[i], edgecolors="k", alpha=0.7)
#
# # --- Plot Bottom 5: line fixed, markers colored ---
# plt.plot(bottom5_hosp["ALOS"], bottom5_hosp["net_profit_margin(%)"], color="red", linestyle="-")
# for i in range(len(bottom5_hosp)):
#     plt.scatter(bottom5_hosp["ALOS"].iloc[i], bottom5_hosp["net_profit_margin(%)"].iloc[i],
#                 s=bottom5_hosp["Net_Patient_Revenue_Total"].iloc[i]/1e6,
#                 color=bottom_colors[i], edgecolors="k", alpha=0.7)
#
# # --- Create custom legend elements ---
# legend_elements = []
#
# # Line legends
# legend_elements.append(Line2D([0], [0], color='green', lw=2, label='Top 5 Line'))
# legend_elements.append(Line2D([0], [0], color='red', lw=2, label='Bottom 5 Line'))
#
# # Marker legends for hospitals
# for i in range(len(top5)):
#     legend_elements.append(Line2D([0], [0], marker='o', color='w', label=custom_labels[i],
#                                   markerfacecolor=top_colors[i], markersize=8, markeredgecolor='k'))
#
# for i in range(len(bottom5)):
#     legend_elements.append(Line2D([0], [0], marker='o', color='w', label=custom_labels[i+5],
#                                   markerfacecolor=bottom_colors[i], markersize=8, markeredgecolor='k'))
#
# # --- Labels & Styling ---
# plt.xlabel("Average Length of Stay (ALOS)")
# plt.ylabel("Net Profit Margin (%)")
# plt.title("Top vs Bottom 5 Hospitals: ALOS vs Profitability (Markers Colored, Names in Legend)")
# plt.grid(alpha=0.3)
#
# # --- Legend outside the plot ---
# plt.legend(handles=legend_elements, bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, frameon=True)
#
# plt.tight_layout()  # ensures nothing is cut
# plt.show()
#
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import matplotlib.ticker as mtick
#
#
# # --- Colors for stacked bars ---
# inpatient_color = "#1f77b4"
# outpatient_color = "#ff7f0e"
#
# plt.figure(figsize=(12,6))
# combined["Gross_Inpatient_Cr"] = combined["Gross_Inpatient_Revenue_Total_Patient_Revenue"] / 1e7
# combined["Gross_Outpatient_Cr"] = combined["Gross_Outpatient_Revenue_Total_Patient_Revenue"] / 1e7
# combined["Gross_patient_revenue"]=combined["Gross_Patient_Revenue_Total_Patient_Revenue"]/1e7
# combined["Overall Gross revenue"] = combined["Summary_of_Revenue_and_Costs_Net_Revenue_Totals_/_Net_Profit_(Loss)"] / 1e7
#
#
# # --- Stacked bars ---
# bars1 = plt.bar(combined.index,combined["Gross_Inpatient_Cr"],
#                 color=inpatient_color, label="Inpatient Revenue")
# bars2 = plt.bar(combined.index,combined["Gross_Outpatient_Cr"] ,
#                 bottom=combined["Gross_Inpatient_Cr"],
#                 color=outpatient_color, label="Outpatient Revenue")
#
# # # --- Overlay Total Gross Revenue line ---
# plt.plot(combined.index,combined["Gross_patient_revenue"] , color="green", marker='o', linestyle='-', label="Total Gross Revenue")
# plt.plot(combined.index, combined["Overall Gross revenue"], color="red", marker='o', linestyle='-', label="Overall Gross Revenue")
#
# # --- Add Net Profit Margin labels on top of each stacked bar ---
# y_offset = combined["Summary_of_Revenue_and_Costs_Net_Revenue_Totals_/_Net_Profit_(Loss)"].max() * 0.02  # 2% of max revenue for padding
#
# for i in range(len(combined)):
#     top_of_bar = combined["Gross_Inpatient_Cr"].iloc[i] + combined["Gross_Outpatient_Cr"].iloc[i]
#     plt.text(i, top_of_bar + y_offset, f"{combined['net_profit_margin(%)'].iloc[i]:.1f}%",
#              ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')
#
# plt.xticks(combined.index, custom_labels,ha='right')
#
# plt.xlabel("Hospitals (Top 5 + Bottom 5)")
# plt.ylabel("Revenue (in crores)")
# plt.title("Hospital Revenue: Inpatient vs Outpatient (Total Gross Overlay)")
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# plt.grid(alpha=0.3, axis='y')
# plt.subplots_adjust(left=0.1, right=0.75, top=0.9, bottom=0.2)
# # --- Format y-axis as integers, no scientific notation ---
# plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f'))
# plt.tight_layout(pad=2.0)
# plt.show()



# import pandas as pd
# import plotly.express as px
# df=pd.read_excel('California_dataset.xlsx')
#
# # Prepare DataFrame
# combined1= df[[
#     "Health_Care_Institution_(Legal_Name)",
#     "Summary_of_Revenue_and_Costs_Net_Revenue_Totals_/_Net_Profit_(Loss)",
#     "Summary_of_Revenue_and_Costs_Net_Revenue_Minus_Net_Costs_Totals_/_Net_Profit_(Loss)"
# ]].copy()
#
# # Convert to crores
# combined1["Net_Revenue_Cr"] = combined1.iloc[:,1] / 1e7
# combined1["Net_Profit_Cr"] = combined1.iloc[:,2] / 1e7
#
# # Melt for Plotly
# combined_melt = combined1.melt(
#     id_vars="Health_Care_Institution_(Legal_Name)",
#     value_vars=["Net_Revenue_Cr", "Net_Profit_Cr"],
#     var_name="Metric",
#     value_name="Amount"
# )
#
# # Diverging horizontal bar chart
# fig = px.bar(
#     combined_melt,
#     x="Amount",
#      y="Health_Care_Institution_(Legal_Name)",
#     color="Metric",
#     orientation='h',
#     hover_data={"Amount":":.2f", "Health_Care_Institution_(Legal_Name)":True},
#     color_discrete_map={"Net_Revenue_Cr":"steelblue", "Net_Profit_Cr":"darkred"}
# )
#
# fig.update_layout(
#     title="All 75 Hospitals – Net Revenue vs Net Profit/Loss (Interactive Diverging Bar)",
#     xaxis_title="Amount (Crores ₹)",
#     yaxis_title="",   # hide axis title for cleanliness     yaxis={'categoryorder':'total ascending'},  # optional: sort by total
#      template="plotly_white",
#     height=2200)
# fig.show()
#
#
#

# import matplotlib.ticker as mtick
# # --- Colors for stacked bars ---
# inpatient_color = "#1f77b4"
# outpatient_color = "#ff7f0e"
# # --- convert to crores ---
#
# combined["Gross_Inpatient_Cr"] = combined["Gross_Inpatient_Revenue_Total_Patient_Revenue"] / 1e7
# combined["Gross_Outpatient_Cr"] = combined["Gross_Outpatient_Revenue_Total_Patient_Revenue"] / 1e7
# combined["Total_Gross_Cr"] = combined["Gross_Patient_Revenue_Total_Patient_Revenue"] / 1e7
#
#
# plt.figure(figsize=(12,6))
#
# # --- Stacked bars ---
# bars1 = plt.bar(combined.index, combined["Gross_Inpatient_Revenue_Total_Patient_Revenue"],
#                 color=inpatient_color, label="Inpatient Revenue")
# bars2 = plt.bar(combined.index, combined["Gross_Outpatient_Revenue_Total_Patient_Revenue"],
#                 bottom=combined["Gross_Inpatient_Revenue_Total_Patient_Revenue"],
#                 color=outpatient_color, label="Outpatient Revenue")
#
# # --- Overlay Total Pat_Gross Revenue and Overall gross revenue line ---
# plt.plot(combined.index, combined["Gross_Patient_Revenue_Total_Patient_Revenue"], color="green", marker='o', linestyle='-', label="Total Pat_Gross Revenue")
# plt.plot(combined.index, combined["Summary_of_Revenue_and_Costs_Net_Revenue_Totals_/_Net_Profit_(Loss)"], color="red", marker='o', linestyle='-', label="Overall_Gross Revenue")
#
# # --- met profit margin on top---
# for i in range(len(combined)):
#     # Get the top of the stacked bar
#     top_of_bar = combined["Gross_Inpatient_Cr"].iloc[i] + combined["Gross_Outpatient_Cr"].iloc[i]
#
#     # Add Net Profit Margin as text
#     plt.text(i, top_of_bar + 0.5, f"{combined['net_profit_margin(%)'].iloc[i]:.1f}%",
#              ha='center', va="bottom",fontsize=9.5, fontweight='bold', color='black')
#
# plt.xticks(combined.index, custom_labels,rotation=45)
#
# plt.xlabel("Hospitals (Top 5 + Bottom 5)")
# plt.ylabel("Revenue (in crores)")
# plt.title("Hospital Revenue: Inpatient vs Outpatient (Total Gross Overlay)")
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f'))
# plt.grid(alpha=0.3, axis='y')
# plt.tight_layout()
# plt.show()

#treemap
# import pandas as pd
# import plotly.express as px
# import plotly.io as pio
#
# # Force browser renderer
# pio.renderers.default = "browser"
#
# service_cols = [
#     'Expenses_Salaries_and_Wages_Total_Patient_Care_Services',
#     'Expenses_Employee_Benefits_Total_Patient_Care_Services',
#     'Expenses_Professional_Fees_Total_Patient_Care_Services',
#     'Expenses_Supplies_Total_Patient_Care_Services',
#     'Expenses_Reclassified_Physician_and_Student_Compensation_Total_Patient_Care_Services',
#     'Expenses_Purchased_Services_Total_Patient_Care_Services',
#     'Expenses_Depreciation_Total_Patient_Care_Services',
#     'Expenses_Leases_and_Rentals_Total_Patient_Care_Services',
#     'Expenses_Other_Direct_Expenses_Total_Patient_Care_Services',
#     'Expenses_Adjustment_of_Direct_Expenses_Page_14Total_Patient_Care_Services'
# ]
#
top5['group'] = 'Top 5 Hospitals'
bottom5['group'] = 'Bottom 5 Hospitals'

combined = pd.concat([top5, bottom5], ignore_index=True)

# df_long = combined.melt(
#     id_vars=['Health_Care_Institution_(Legal_Name)', 'net_profit_margin(%)', 'group', 'Expenses_Adjusted_Direct_Expenses_Total_Patient_Care_Services'],
#     value_vars=service_cols,
#     var_name='comp',
#     value_name='expense'
# )
# df_long['hosp_label'] = df_long['Health_Care_Institution_(Legal_Name)'] + " (" + df_long['net_profit_margin(%)'].round(2).astype(str) + "%)"
#
# fig = px.treemap(
#     df_long,
#     path=['group', 'hosp_label', 'comp'],
#     values='expense',
#     color='net_profit_margin(%)',
#     color_continuous_scale='Viridis',
#     title="Top 5 vs Bottom 5 Hospitals Treemap",
#     hover_data={'net_profit_margin(%)':False,'group':False}
# )
# fig.update_traces(textinfo='label+value')
# import numpy as np
#
# # Get colors array (numeric) from Plotly
# colors = np.array(fig.data[0]['marker']['colors'], dtype=object)
#
# # Replace parent group colors
# for i, node_id in enumerate(fig.data[0]['ids']):
#     if node_id == "Top 5 Hospitals":
#         colors[i] = "rgb(0,200,0)"   # green
#     elif node_id == "Bottom 5 Hospitals":
#         colors[i] = "rgb(200,0,0)"   # red
#
# # Assign back
# fig.data[0]['marker']['colors'] = colors
#
#
# fig.show()
# Heat map
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from bokeh.plotting import output_file
# output_file("heatmap.html")
#
#
# # --- Load your dataframe ---
# # df = pd.read_csv("your_file.csv")
#
# # Expense component columns
# expense_cols = [
#     "Expenses_Salaries_and_Wages_Total_Costs",
#     "Expenses_Employee_Benefits_Total_Costs",
#     "Expenses_Reclassified_Physician_and_Student_Compensation_Total_Costs",
#     "Expenses_Professional_Fees_Total_Costs",
#     "Expenses_Supplies_Total_Costs",
#     "Expenses_Purchased_Services_Total_Costs",
#     "Expenses_Depreciation_Total_Costs",
#     "Expenses_Leases_and_Rentals_Total_Costs",
#     "Expenses_Other_Direct_Expenses_Total_Costs"
# ]
#
#  # Normalize expenses as % of Adjusted Direct Expenses
# for col in expense_cols:
#     combined[col] = (combined[col] / combined["Expenses_Adjusted_Direct_Expenses_Total_Costs"]) * 100
#
# # Melt for heatmap format
# heatmap_data = combined.melt(
#     id_vars=["Health_Care_Institution_(Legal_Name)"],
#     value_vars=expense_cols,
#     var_name="Expense_Type",
#     value_name="Percent_of_Total"
# )
#
# # Pivot into matrix
# heatmap_matrix = heatmap_data.pivot(
#     index="Expense_Type",
#     columns="Health_Care_Institution_(Legal_Name)",
#     values="Percent_of_Total"
# )
#
# # Plot heatmap
# fig_width = max(12, len(heatmap_matrix.columns) * 1.5)  # adjust 0.8 to control box width
# fig_height = max(6, len(heatmap_matrix.index) * 0.5)   # adjust 0.5 to control box height
#
# fig, ax = plt.subplots(figsize=(fig_width, fig_height))
#
#
# sns.heatmap(
#     heatmap_matrix,
#     cmap="YlOrRd",  # Yellow→Orange→Red scale
#     annot=True, fmt=".1f",
#     cbar_kws={'label': '% of Adjusted Direct Expenses'},
#     xticklabels=custom_labels)
#
# # 2. Move x-axis labels to the top
# ax.xaxis.tick_top()
# ax.xaxis.set_label_position('top')
# ax.set_xlabel(ax.get_xlabel(), labelpad=20)  # push x-axis label slightly up
# plt.suptitle("Top & Bottom 5 Hospitals by Net Profit Margin – Expense Breakdown (%)",fontsize=16, fontweight='bold', x=0.5)
# plt.xlabel("HOSPITALS",fontweight='bold',color='orange')
# plt.ylabel("EXPENSE COMPONENTS",fontweight='bold',color='orange')
# plt.tight_layout()  # adjust horizontal padding to center heatmap
#
# plt.show()
# donut chart
# combined['Expenses_Adjusted_Direct_Expenses_Total_remaining_costs'] = \
#     combined['Expenses_Adjusted_Direct_Expenses_Total_Costs'] - \
#   combined['Expenses_Adjusted_Direct_Expenses_Total_Patient_Care_Services']
# import matplotlib.pyplot as plt
#
# fig, axes = plt.subplots(5, 2, figsize=(16, 12))  # 5 rows, 2 columns
#
# top_hospitals = combined.iloc[:5]    # first 5 rows: top5
# bottom_hospitals = combined.iloc[5:] # next 5 rows: bottom5
#
# for i in range(5):
#     # Top 5 donut
#     values = [top_hospitals.iloc[i]['Expenses_Adjusted_Direct_Expenses_Total_Patient_Care_Services'],
#               top_hospitals.iloc[i]['Expenses_Adjusted_Direct_Expenses_Total_remaining_costs']]
#     axes[i,0].pie(values, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3),pctdistance=1.5)
#     axes[i,0].set_title(top_hospitals.iloc[i]['Health_Care_Institution_(Legal_Name)'], fontsize=10,fontweight='bold',fontstyle='italic')
#
#     # Bottom 5 donut
#     values = [bottom_hospitals.iloc[i]['Expenses_Adjusted_Direct_Expenses_Total_Patient_Care_Services'],
#               bottom_hospitals.iloc[i]['Expenses_Adjusted_Direct_Expenses_Total_remaining_costs']]
#     axes[i,1].pie(values,autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3),pctdistance=1.5)
#     axes[i,1].set_title(bottom_hospitals.iloc[i]['Health_Care_Institution_(Legal_Name)'], fontsize=10,fontweight='bold',fontstyle='italic')
# # labels=['Patient Care costs','Remaining costs']
# # plt.legend(labels, loc="lower left",bbox_to_anchor=(1.02, 1))
# # After plotting all your donuts
# fig.legend(["Patient Care Services", "Remaining Costs"],
#            loc="upper left",
#            ncol=1,                        # keep items stacked vertically
#            fontsize=9,
#            frameon=True)
#
# fig.suptitle('Top & Bottom 5 Hospitals Expense distribution',fontweight='bold',fontstyle='italic',y=1)
# plt.tight_layout(rect=[0, 0, 0.90, 0.95])
# plt.show()
# dumbbell chart
# import matplotlib.ticker as mtick
# bottom5_reversed = bottom5.iloc[::-1]
#
# # Concatenate top5 + reversed bottom5
# dumbbell_df = pd.concat([top5, bottom5_reversed]).reset_index(drop=True)
#
# y_pos = range(len(dumbbell_df))
# fig,ax = plt.subplots(figsize=(10,5))
# fig.subplots_adjust(left=0.30, right=0.88, top=0.9, bottom=0.1)  # tweak left to shift left
#
#
#  # Dumbbell lines
# ax.hlines(y=y_pos,
#           xmin=dumbbell_df['Net_Patient_Revenue_Total'],
#           xmax=dumbbell_df['Gross_Patient_Revenue_Total_Patient_Revenue'],
#           color='lightgray', linewidth=2)
#
# # Points
# ax.plot(dumbbell_df['Gross_Patient_Revenue_Total_Patient_Revenue'], y_pos, 'o', color='#1f77b4', label='Gross Revenue')
# ax.plot(dumbbell_df['Net_Patient_Revenue_Total'], y_pos, 'o', color='#ff7f0e', label='Net Revenue')
#
# # Y-axis labels = Hospital Names
# ax.set_yticks(y_pos)
# ax.set_yticklabels(dumbbell_df['Health_Care_Institution_(Legal_Name)'], fontsize=9)
#
# ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{x/1e7:.1f} Cr'))
#
# # Labels and title
# ax.set_xlabel('Revenue (in Crores)', fontsize=12)
# plt.suptitle('Gross vs Net Patient Revenue: Top & Bottom 5 Hospitals by Net Profit Margin', fontsize=14, fontweight='bold')
#
# # Legend
# ax.legend(loc='upper right')
#
# plt.show()
# stacked bar
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# # # Columns to stack
# cols = ['Summary_of_Revenue_and_Costs_Net_Revenue_Totals_/_Net_Profit_(Loss)',
# 'Summary_of_Revenue_and_Costs_Net_Costs_as_Reallocated_Totals_/_Net_Profit_(Loss)',
# 'Summary_of_Revenue_and_Costs_Net_Revenue_Minus_Net_Costs_Totals_/_Net_Profit_(Loss)']
#
# y=np.arange(len(combined))
#
# width = 0.6
#
# fig, ax = plt.subplots(figsize=(12,6))
#
# bottom = np.zeros(len(combined))
#
# # # First two stacks with any color
# ax.bar(y, combined[cols[0]], bottom=bottom, color='skyblue', label=cols[0])
# bottom += combined[cols[0]]
#
# ax.bar(y, combined[cols[1]], bottom=bottom, color='orange', label=cols[1])
# bottom += combined[cols[1]]
#
# # Last stack red if negative, green if positive
# colors = ['green' if val >= 0 else 'red' for val in combined[cols[2]]]
# bars=ax.bar(y, combined[cols[2]], bottom=bottom, color=colors, label=cols[2])
# labels = [f'{v/1e7:.2f} Cr' for v in combined['Summary_of_Revenue_and_Costs_Net_Revenue_Minus_Net_Costs_Totals_/_Net_Profit_(Loss)'].values]  # in Crores
# ax.bar_label(bars, labels=labels,label_type='edge', padding=3, fontsize=9, fontweight='bold')
#
# ax.set_ylabel('Amount',fontweight='bold')
# ax.set_xlabel('Hospitals',fontweight='bold')
# ax.set_title('Top 5 and Bottom 5 Hospitals by Net Profit/loss',fontweight='bold')
# ax.set_xticks(x)
# ax.set_xticklabels(custom_labels, rotation=45, ha='right')
# ax.legend()
# import matplotlib.ticker as mtick
#
# # # Format y-axis in crores
# ax.yaxis.set_major_formatter(
#     mtick.FuncFormatter(lambda x, _: f'{x/1e7:.0f} Cr'))
# plt.tight_layout()
# plt.show()
#
import pandas as pd

# Suppose 'bottom5' is your bottom 5 DataFrame
# Reverse the order
bottom5_reversed = bottom5.iloc[::-1]

# Combine with top5 (assuming you already have top5)
top_bottom = pd.concat([top5, bottom5_reversed])

# Save to Excel
top_bottom.to_excel("top_bottom_5_hospitals.xlsx", index=False)


