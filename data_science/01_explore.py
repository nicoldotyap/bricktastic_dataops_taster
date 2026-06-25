"""
STEP 1 — Explore the Engineered Data
======================================
We start from the enriched dataset produced by the data engineering pipeline.
This is richer than the raw data — sets already have theme names, complexity
tiers, decade labels, and era labels joined in.

This step covers:
  - Loading the enriched dataset
  - Visualising sets per year
  - Exploring complexity and era distributions
  - Top themes by number of sets
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- Load enriched data from data engineering pipeline ---
enriched = pd.read_csv("../data_engineering/enriched_sets.csv")

print("Shape:", enriched.shape)
print("\nFirst 5 rows:")
print(enriched.head())

print("\nColumn types:")
print(enriched.dtypes)

print("\nMissing values:")
print(enriched.isnull().sum())

print("\nYear range:", enriched["year"].min(), "to", enriched["year"].max())

# --- Chart 1: How many LEGO sets were released each year? ---
sets_per_year = enriched.groupby("year").size().reset_index(name="count")

plt.figure(figsize=(12, 5))
plt.plot(sets_per_year["year"], sets_per_year["count"], color="red", linewidth=2)
plt.title("LEGO Sets Released Per Year (from engineered data)")
plt.xlabel("Year")
plt.ylabel("Number of Sets")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart_sets_per_year.png")
plt.show()
print("Chart saved: chart_sets_per_year.png")

# --- Chart 2: Average number of parts per set over time ---
avg_parts = enriched.groupby("year")["num_parts"].mean().reset_index()

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
top_themes = enriched["theme_name"].value_counts().head(10)

plt.figure(figsize=(10, 5))
top_themes.plot(kind="barh", color="steelblue")
plt.title("Top 10 LEGO Themes by Number of Sets")
plt.xlabel("Number of Sets")
plt.tight_layout()
plt.savefig("chart_top_themes.png")
plt.show()
print("Chart saved: chart_top_themes.png")

# --- Chart 4: Complexity tier distribution (bonus — not in original track) ---
complexity_counts = enriched["complexity"].value_counts()

plt.figure(figsize=(8, 5))
complexity_counts.plot(kind="bar", color="orange", edgecolor="black")
plt.title("LEGO Sets by Complexity Tier")
plt.xlabel("Complexity")
plt.ylabel("Number of Sets")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_complexity.png")
plt.show()
print("Chart saved: chart_complexity.png")

print("\n✅ Exploration complete! Check the charts above.")
print("💡 Question: How does this data compare to exploring the raw CSV directly?")
