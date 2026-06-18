"""
STEP 1 — Explore the Data
=========================
Before building any model, data scientists always start by understanding the data.
Run this file and look at the charts. What patterns do you notice?
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- Load data ---
sets = pd.read_csv("../data/lego_sets.csv")
themes = pd.read_csv("../data/lego_themes.csv")

print("Shape:", sets.shape)
print("\nFirst 5 rows:")
print(sets.head())

print("\nColumn types:")
print(sets.dtypes)

print("\nMissing values:")
print(sets.isnull().sum())

print("\nYear range:", sets["year"].min(), "to", sets["year"].max())

# --- Chart 1: How many LEGO sets were released each year? ---
sets_per_year = sets.groupby("year").size().reset_index(name="count")

plt.figure(figsize=(12, 5))
plt.plot(sets_per_year["year"], sets_per_year["count"], color="red", linewidth=2)
plt.title("LEGO Sets Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Sets")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart_sets_per_year.png")
plt.show()
print("Chart saved: chart_sets_per_year.png")

# --- Chart 2: Average number of parts per set over time ---
avg_parts = sets.groupby("year")["num_parts"].mean().reset_index()

plt.figure(figsize=(12, 5))
plt.bar(avg_parts["year"], avg_parts["num_parts"], color="yellow", edgecolor="black", alpha=0.7)
plt.title("Average Number of Parts Per Set Over Time")
plt.xlabel("Year")
plt.ylabel("Average Parts")
plt.grid(True, alpha=0.3, axis="y")
plt.tight_layout()
plt.savefig("chart_avg_parts.png")
plt.show()
print("Chart saved: chart_avg_parts.png")

# --- Chart 3: Top 10 themes by number of sets ---
sets_with_themes = sets.merge(themes, on="theme_id", how="left")
top_themes = sets_with_themes["name_y"].value_counts().head(10)

plt.figure(figsize=(10, 5))
top_themes.plot(kind="barh", color="steelblue")
plt.title("Top 10 LEGO Themes by Number of Sets")
plt.xlabel("Number of Sets")
plt.tight_layout()
plt.savefig("chart_top_themes.png")
plt.show()
print("Chart saved: chart_top_themes.png")

print("\n✅ Exploration complete! Check the charts above.")
print("💡 Question: What year did LEGO release the most sets?")
