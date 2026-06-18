"""
STEP 2 — Clean the Data
=========================
Raw data is messy. Data engineers clean it before it can be used downstream.

This step covers:
  - Standardising column names
  - Handling missing values
  - Fixing data types
  - Removing invalid records
"""

import pandas as pd

# --- Load raw snapshots from step 1 ---
sets   = pd.read_csv("raw_sets.csv")
themes = pd.read_csv("raw_themes.csv")
colors = pd.read_csv("raw_colors.csv")

print("Starting shapes:")
print(f"  sets:   {sets.shape}")
print(f"  themes: {themes.shape}")
print(f"  colors: {colors.shape}")

# ── Clean: sets ──────────────────────────────────────────────────────────────

# Standardise column names to lowercase with underscores
sets.columns = [c.strip().lower().replace(" ", "_") for c in sets.columns]

# Remove sets with no year or clearly invalid year
before = len(sets)
sets = sets[sets["year"].notna()]
sets = sets[(sets["year"] >= 1949) & (sets["year"] <= 2030)]
print(f"\nSets: removed {before - len(sets)} rows with invalid year")

# Fill missing num_parts with 0 (unknown part count, not absent)
sets["num_parts"] = sets["num_parts"].fillna(0).astype(int)

# Standardise set names — strip whitespace, title case
sets["name"] = sets["name"].str.strip().str.title()

# Cast year to int
sets["year"] = sets["year"].astype(int)

print(f"Sets after cleaning: {sets.shape}")

# ── Clean: themes ────────────────────────────────────────────────────────────

themes.columns = [c.strip().lower().replace(" ", "_") for c in themes.columns]
themes["name"] = themes["name"].str.strip().str.title()

# Fill missing parent_id with -1 (top-level theme has no parent)
themes["parent_id"] = themes["parent_id"].fillna(-1).astype(int)

print(f"Themes after cleaning: {themes.shape}")

# ── Clean: colors ────────────────────────────────────────────────────────────

colors.columns = [c.strip().lower().replace(" ", "_") for c in colors.columns]
colors["name"] = colors["name"].str.strip().str.title()

# Standardise is_transparent to boolean
colors["is_transparent"] = colors["is_transparent"].map(
    {"True": True, "False": False, True: True, False: False}
)

# Ensure rgb is uppercase and 6 characters
colors["rgb"] = colors["rgb"].str.upper().str.strip()

print(f"Colors after cleaning: {colors.shape}")

# --- Save cleaned data ---
sets.to_csv("clean_sets.csv", index=False)
themes.to_csv("clean_themes.csv", index=False)
colors.to_csv("clean_colors.csv", index=False)

print("\nCleaned files saved: clean_sets.csv, clean_themes.csv, clean_colors.csv")
print("\n✅ Cleaning complete!")
print("💡 Question: Why do we save cleaned data as a separate file rather than overwriting the raw?")
