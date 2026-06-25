"""
STEP 3 — Train a Forecasting Model
=====================================
We train a Linear Regression model to forecast how many LEGO sets will be
released in future years, using the features built in step 2.

The data here comes from the clean, engineered pipeline rather than raw CSVs,
meaning the model trains on validated, consistently-typed data.

This step covers:
  - Defining input features and target
  - Train/test split (keeping time order)
  - Training a Linear Regression model
  - Saving the model for evaluation
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- Load features from step 2 ---
df = pd.read_csv("features.csv")

print("Features available:")
print(df.columns.tolist())

# --- Define input features (X) and target (y) ---
FEATURES = ["year", "lag_1", "lag_2", "rolling_3yr_avg", "rolling_5yr_avg"]
TARGET = "sets_count"

X = df[FEATURES]
y = df[TARGET]

# --- Train/test split (80% train, 20% test, shuffle=False keeps time order) ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

print(f"\nTraining rows: {len(X_train)}")
print(f"Test rows:     {len(X_test)}")
print(f"\nTraining years: {X_train['year'].min()} to {X_train['year'].max()}")
print(f"Test years:     {X_test['year'].min()} to {X_test['year'].max()}")

# --- Train the model ---
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel trained!")
print("\nFeature coefficients (how much each feature influences the prediction):")
for feat, coef in zip(FEATURES, model.coef_):
    print(f"  {feat:25s}: {coef:+.3f}")
print(f"  {'intercept':25s}: {model.intercept_:+.3f}")

# --- Save model and test split ---
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

X_test.to_csv("X_test.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("\nModel saved: model.pkl")
print("Test data saved: X_test.csv, y_test.csv")
print("\n✅ Training complete!")
print("💡 Question: Why do we NOT shuffle the data before splitting for time series?")
