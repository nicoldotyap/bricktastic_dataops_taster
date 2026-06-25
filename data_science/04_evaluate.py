"""
STEP 4 — Evaluate the Model
==============================
A model is only useful if it's accurate. We measure performance using:

- MAE  (Mean Absolute Error):   average number of sets we're off by
- RMSE (Root Mean Squared Error): penalises large errors more heavily
- R²   (R-squared): how much of the variation our model explains (1.0 = perfect)

We also plot actual vs predicted to visually inspect the fit.
"""

import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- Load model and test data ---
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

X_test = pd.read_csv("X_test.csv")
y_test = pd.read_csv("y_test.csv").squeeze()

# --- Make predictions ---
y_pred = model.predict(X_test)

# --- Calculate metrics ---
mae  = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2   = r2_score(y_test, y_pred)

print("=" * 40)
print("MODEL PERFORMANCE")
print("=" * 40)
print(f"MAE  (avg sets off by):    {mae:.1f}")
print(f"RMSE (penalises outliers): {rmse:.1f}")
print(f"R²   (explains variance):  {r2:.3f}")
print("=" * 40)

if r2 > 0.8:
    print("✅ Good fit — the model explains most of the variation.")
elif r2 > 0.5:
    print("⚠️  Moderate fit — room for improvement.")
else:
    print("❌ Weak fit — consider adding more features.")

# --- Chart: Actual vs Predicted ---
results = pd.DataFrame({
    "year":      X_test["year"].values,
    "actual":    y_test.values,
    "predicted": y_pred,
})

plt.figure(figsize=(10, 5))
plt.plot(results["year"], results["actual"],    "o-", label="Actual",    color="red")
plt.plot(results["year"], results["predicted"], "s--", label="Predicted", color="blue")
plt.fill_between(results["year"], results["actual"], results["predicted"], alpha=0.1, color="gray")
plt.title("Actual vs Predicted — LEGO Sets Per Year (engineered data)")
plt.xlabel("Year")
plt.ylabel("Number of Sets")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart_actual_vs_predicted.png")
plt.show()

print("\nChart saved: chart_actual_vs_predicted.png")
print("\n✅ Evaluation complete!")
print("💡 Question: Where does the model perform worst? What might cause that?")
