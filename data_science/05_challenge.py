"""
STEP 5 — YOUR CHALLENGE 🏆
============================
You've explored engineered data, built features, trained a model, and evaluated it.
Now use the model to predict the future — AND use the richer engineered data
to make a better forecast.

YOUR TASK:
  Use the trained model to forecast how many LEGO sets will be released
  in the next 5 years (from the last year in the dataset).

BONUS: The enriched data has complexity tiers and era labels.
  Can you build a second chart showing predicted complexity breakdown
  for the forecast years? Use the distribution from output_by_decade.csv
  as a reference.

HINTS:
  - Load model.pkl using pickle
  - Load features.csv to get the last known lag/rolling values
  - Load ../data_engineering/output_by_decade.csv for richer context
  - Build a DataFrame of future years and call model.predict()
  - Plot historical + forecast with a vertical dashed line separator

Good luck! 🧱
"""

import pandas as pd
import matplotlib.pyplot as plt
import pickle
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- Load the trained model ---
# TODO: load model.pkl using pickle
model = None  # replace this line


# --- Load historical features ---
# TODO: load features.csv into a DataFrame called df
df = None  # replace this line


# --- Load the aggregated decade summary for bonus context ---
# TODO: load ../data_engineering/output_by_decade.csv into by_decade
by_decade = None  # replace this line
print("Decade summary from data engineering:")
print(by_decade)


# --- Get the last known values ---
# TODO: get the last row of df to use as starting point
last_row  = None  # replace this line
last_year = None  # replace this line


# --- Build future years ---
# TODO: create a list of the next 5 years after last_year
future_years = []  # e.g. [2011, 2012, 2013, 2014, 2015]


# --- Build a DataFrame for future predictions ---
# HINT: use the last known lag/rolling values as estimates to start
future_rows = []
for year in future_years:
    row = {
        "year":            year,
        "lag_1":           None,   # TODO: fill in
        "lag_2":           None,   # TODO: fill in
        "rolling_3yr_avg": None,   # TODO: fill in
        "rolling_5yr_avg": None,   # TODO: fill in
    }
    future_rows.append(row)

future_df = pd.DataFrame(future_rows)
print("\nFuture input:")
print(future_df)


# --- Make predictions ---
# TODO: use model.predict() on future_df and store results
predictions = None  # replace this line


# --- Print results ---
print("\nForecast:")
for year, pred in zip(future_years, predictions):
    print(f"  {year}: {pred:.0f} sets predicted")


# --- Plot historical + forecast ---
plt.figure(figsize=(12, 5))

# Historical line
# TODO: plt.plot(df["year"], df["sets_count"], ...)

# Forecast line
# TODO: plt.plot(future_years, predictions, ...)

# Vertical separator between history and forecast
# TODO: plt.axvline(x=last_year, linestyle="--", color="gray", label="Forecast start")

plt.title("LEGO Sets — Historical + 5-Year Forecast (from engineered data)")
plt.xlabel("Year")
plt.ylabel("Number of Sets")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart_forecast.png")
plt.show()

print("\n🏆 Challenge complete! How accurate do you think your forecast is?")
print("💡 Bonus: Does using clean engineered data change the forecast vs raw data?")
