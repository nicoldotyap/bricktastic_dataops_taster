"""
STEP 2 — Feature Engineering
=============================
Raw data is rarely ready for a model. We need to create "features" —
meaningful signals the model can learn from.

Here we build lag features and rolling averages from the yearly set counts.
These help the model understand trends and momentum over time.
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- Load and aggregate ---
sets = pd.read_csv("../data/lego_sets.csv")
df = sets.groupby("year").size().reset_index(name="sets_count")
df = df.sort_values("year").reset_index(drop=True)

print("Yearly set counts:")
print(df.head(10))

# --- Feature 1: Lag features (last year's count, 2 years ago) ---
# A lag feature tells the model what happened in previous years
df["lag_1"] = df["sets_count"].shift(1)   # previous year
df["lag_2"] = df["sets_count"].shift(2)   # 2 years ago

# --- Feature 2: Rolling average (smooth out noise) ---
# Rolling average shows the general trend over a window of years
df["rolling_3yr_avg"] = df["sets_count"].rolling(window=3).mean()
df["rolling_5yr_avg"] = df["sets_count"].rolling(window=5).mean()

# --- Feature 3: Year-on-year growth ---
df["yoy_growth"] = df["sets_count"].pct_change() * 100  # as percentage

# --- Drop rows with NaN (from lag/rolling) ---
df = df.dropna().reset_index(drop=True)

print("\nFeature-engineered data:")
print(df.head(10))
print(f"\nDataset shape after feature engineering: {df.shape}")

# --- Save for next step ---
df.to_csv("features.csv", index=False)
print("\nFeatures saved to: features.csv")

# --- Chart: Actual vs rolling average ---
plt.figure(figsize=(12, 5))
plt.plot(df["year"], df["sets_count"], label="Actual", color="red", alpha=0.6)
plt.plot(df["year"], df["rolling_3yr_avg"], label="3-Year Rolling Avg", color="blue", linewidth=2)
plt.plot(df["year"], df["rolling_5yr_avg"], label="5-Year Rolling Avg", color="green", linewidth=2)
plt.title("LEGO Sets Per Year — Actual vs Rolling Averages")
plt.xlabel("Year")
plt.ylabel("Number of Sets")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart_rolling_avg.png")
plt.show()

print("\n✅ Feature engineering complete!")
print("💡 Question: Why do we use rolling averages? What does smoothing help with?")
