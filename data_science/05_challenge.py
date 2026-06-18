"""
STEP 5 — YOUR CHALLENGE 🏆
============================
You've explored the data, engineered features, trained a model, and evaluated it.
Now it's your turn to use the model to predict the future!

YOUR TASK:
  Use the trained model to forecast how many LEGO sets will be released
  in the next 5 years (from the last year in the dataset).

HINTS:
  - Load the model from model.pkl
  - Load the features from features.csv to get the last known values
  - Build a new DataFrame with future years and estimated lag/rolling values
  - Call model.predict() on your future DataFrame
  - Plot the historical data + your forecast

Good luck! 🧱
"""

import pandas as pd
import matplotlib.pyplot as plt
import pickle

# --- Load the trained model ---
# TODO: load model.pkl using pickle
model = None  # replace this line


# --- Load historical features ---
# TODO: load features.csv into a DataFrame called df
df = None  # replace this line


# --- Get the last known values ---
# TODO: get the last row of df to use as starting point
last_row = None  # replace this line
last_year = None  # replace this line


# --- Build future years ---
# TODO: create a list of the next 5 years after last_year
future_years = []  # e.g. [2001, 2002, 2003, 2004, 2005]


# --- Build a DataFrame for future predictions ---
# HINT: you'll need to estimate lag_1, lag_2, rolling_3yr_avg, rolling_5yr_avg
# Start simple: use the last known values as estimates

future_rows = []
for year in future_years:
    row = {
        "year": year,
        "lag_1": None,          # TODO: fill in
        "lag_2": None,          # TODO: fill in
        "rolling_3yr_avg": None, # TODO: fill in
        "rolling_5yr_avg": None, # TODO: fill in
    }
    future_rows.append(row)

future_df = pd.DataFrame(future_rows)
print("Future input:")
print(future_df)


# --- Make predictions ---
# TODO: use model.predict() on future_df and store results
predictions = None  # replace this line


# --- Print results ---
for year, pred in zip(future_years, predictions):
    print(f"  {year}: {pred:.0f} sets predicted")


# --- Plot historical + forecast ---
# TODO: plot df["year"] vs df["sets_count"] for historical
# Then plot future_years vs predictions for the forecast
# Add a vertical dashed line to separate history from forecast

plt.figure(figsize=(12, 5))

# Historical line
# plt.plot(...)

# Forecast line
# plt.plot(...)

# Vertical separator
# plt.axvline(...)

plt.title("LEGO Sets — Historical + 5-Year Forecast")
plt.xlabel("Year")
plt.ylabel("Number of Sets")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart_forecast.png")
plt.show()

print("\n🏆 Challenge complete! How accurate do you think your forecast is?")
