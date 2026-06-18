"""
STEP 3 — Train a Forecasting Model
====================================
Now we train a machine learning model to forecast how many LEGO sets
will be released in future years.

We use Linear Regression — a simple but powerful algorithm that finds
the best straight-line relationship between our features and the target.

Train/test split: we train on older data and test on recent years.
This simulates predicting the future using only the past.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# --- Load features ---
df = pd.read_csv("features.csv")

print("Features available:")
print(df.columns.tolist())

# --- Define input features (X) and target (y) ---
FEATURES = ["year", "lag_1", "lag_2", "rolling_3yr_avg", "rolling_5yr_avg"]
TARGET = "sets_count"

X = df[FEATURES]
y = df[TARGET]

# --- Train/test split (80% train, 20% test) ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False  # shuffle=False keeps time order
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

# --- Save model for next step ---
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# --- Save test split for evaluation ---
X_test.to_csv("X_test.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("\nModel saved: model.pkl")
print("Test data saved: X_test.csv, y_test.csv")
print("\n✅ Training complete!")
print("💡 Question: Why do we NOT shuffle the data before splitting for time series?")
