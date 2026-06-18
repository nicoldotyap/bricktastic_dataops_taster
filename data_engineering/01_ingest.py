"""
STEP 1 — Ingest Raw Data
=========================
Data engineers are the first line of defence. Before data can be used,
we must load it and check it's actually usable.

This step covers:
  - Loading raw CSV files
  - Checking shape, types, and null values
  - Flagging data quality issues
"""

import pandas as pd

RAW_DATA_PATH = "../data/"

def load_and_validate(filepath, name):
    print(f"\n{'='*50}")
    print(f"Loading: {name}")
    print(f"{'='*50}")

    df = pd.read_csv(filepath)

    print(f"Rows:    {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")
    print(f"\nColumn types:")
    print(df.dtypes)

    null_counts = df.isnull().sum()
    null_cols = null_counts[null_counts > 0]
    if len(null_cols) > 0:
        print(f"\n⚠️  Missing values found:")
        for col, count in null_cols.items():
            pct = 100 * count / len(df)
            print(f"   {col}: {count} ({pct:.1f}%)")
    else:
        print("\n✅ No missing values")

    dup_count = df.duplicated().sum()
    if dup_count > 0:
        print(f"\n⚠️  Duplicate rows: {dup_count}")
    else:
        print("✅ No duplicate rows")

    return df

# --- Ingest all three tables ---
sets   = load_and_validate(RAW_DATA_PATH + "lego_sets.csv",   "LEGO Sets")
themes = load_and_validate(RAW_DATA_PATH + "lego_themes.csv", "LEGO Themes")
colors = load_and_validate(RAW_DATA_PATH + "lego_colors.csv", "LEGO Colors")

# --- Summary ---
print("\n" + "="*50)
print("INGESTION SUMMARY")
print("="*50)
print(f"Sets:   {sets.shape[0]:,} rows")
print(f"Themes: {themes.shape[0]:,} rows")
print(f"Colors: {colors.shape[0]:,} rows")

# --- Save raw snapshots (simulate landing zone) ---
sets.to_csv("raw_sets.csv", index=False)
themes.to_csv("raw_themes.csv", index=False)
colors.to_csv("raw_colors.csv", index=False)

print("\nRaw snapshots saved: raw_sets.csv, raw_themes.csv, raw_colors.csv")
print("\n✅ Ingestion complete!")
print("💡 Question: Why is it important to check for nulls and duplicates at ingestion?")
