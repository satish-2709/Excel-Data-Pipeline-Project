import pandas as pd
import os

# Folder path
folder_path = "data"

# All excel files read
files = [f for f in os.listdir(folder_path) if f.endswith(".xlsx")]

all_data = []

for file in files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    df["Month"] = file   # identify which file
    all_data.append(df)

# Combine all data
final_df = pd.concat(all_data)

# Total sales
total_sales = final_df["Sales"].sum()

# Percentage calculation
final_df["Percentage"] = ((final_df["Sales"] / total_sales) * 100).round(2)

# Save output
final_df.to_excel("final_report.xlsx", index=False)

print("Data pipeline completed successfully 🚀")

import matplotlib.pyplot as plt

# Total sales by Name
summary = final_df.groupby("Name")["Sales"].sum()

# Bar chart create
plt.figure()
summary.plot(kind='bar')

plt.title("Sales Distribution")
plt.xlabel("Name")
plt.ylabel("Sales")

# Save chart
plt.savefig("sales_chart.png")

print("Chart generated successfully 📊")