"""
STEP 3 — Train a Classification Model (Music Recommender)
==========================================================
We train a machine learning model to classify songs as liked or disliked
based on audio features like danceability, energy, duration, and more.

We use Logistic Regression — a classification algorithm that predicts
the probability of a binary outcome (like = 1, dislike = 0).

Train/test split: we randomly split the data since songs have no time order.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

# --- Load data ---
df = pd.read_csv("music_data.csv")

print("Columns available:")
print(df.columns.tolist())

# --- Define input features (X) and target (y) ---
# Adjust FEATURES to match the actual column names in your CSV
FEATURES = ["danceability", "energy", "duration", "loudness", "tempo",
            "valence", "acousticness", "instrumentalness", "speechiness"]
TARGET = "like"

# Keep only columns that exist in the CSV
FEATURES = [f for f in FEATURES if f in df.columns]
print(f"\nUsing features: {FEATURES}")

X = df[FEATURES]
y = df[TARGET]

print(f"\nTotal rows: {len(df)}")
print(f"Class distribution:\n{y.value_counts().to_string()}")

# --- Train/test split (80% train, 20% test) ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining rows: {len(X_train)}")
print(f"Test rows:     {len(X_test)}")

# --- Train the model ---
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("\nModel trained!")
print("\nFeature coefficients (positive = pushes toward 'like'):")
for feat, coef in zip(FEATURES, model.coef_[0]):
    print(f"  {feat:25s}: {coef:+.3f}")
print(f"  {'intercept':25s}: {model.intercept_[0]:+.3f}")

# --- Quick evaluation on test set ---
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\nTest accuracy: {acc:.1%}")
print("\nClassification report:")
print(classification_report(y_test, y_pred, target_names=["dislike", "like"]))

# --- Save model for next step ---
with open("model_rec.pkl", "wb") as f:
    pickle.dump(model, f)

# --- Save test split for evaluation ---
X_test.to_csv("X_test_rec.csv", index=False)
y_test.to_csv("y_test_rec.csv", index=False)

print("Model saved: model_rec.pkl")
print("Test data saved: X_test_rec.csv, y_test_rec.csv")
print("\n✅ Training complete!")
print("💡 Question: Why do we use random_state=42 when splitting this data, but NOT for the LEGO time series?")
