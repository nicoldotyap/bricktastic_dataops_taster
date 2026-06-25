"""
STEP 3 — Transform the Data
=============================
Transformation means reshaping and enriching data to make it useful.
This is where data engineers join tables, add derived columns, and
produce a clean, analysis-ready dataset.

This step covers:
  - Joining sets with themes
  - Adding derived columns (decade, complexity tier)
  - Producing a wide enriched table
"""

import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- Load cleaned data ---
sets   = pd.read_csv("clean_sets.csv")
themes = pd.read_csv("clean_themes.csv")

print(f"Sets:   {sets.shape}")
print(f"Themes: {themes.shape}")

# --- Join sets with themes ---
enriched = sets.merge(
    themes[["theme_id", "name"]].rename(columns={"name": "theme_name"}),
    on="theme_id",
    how="left",
)

print(f"\nAfter join: {enriched.shape}")
print(f"Themes matched: {enriched['theme_name'].notna().sum()} / {len(enriched)}")

# --- Derived column 1: decade ---
# Group years into decades for aggregate analysis
enriched["decade"] = (enriched["year"] // 10) * 10
enriched["decade_label"] = enriched["decade"].astype(str) + "s"

# --- Derived column 2: complexity tier ---
# Categorise sets by part count into Simple / Standard / Advanced / Expert
def complexity_tier(num_parts):
    if num_parts == 0:
        return "Unknown"
    elif num_parts < 50:
        return "Simple"
    elif num_parts < 300:
        return "Standard"
    elif num_parts < 1000:
        return "Advanced"
    else:
        return "Expert"

enriched["complexity"] = enriched["num_parts"].apply(complexity_tier)

# --- Derived column 3: era ---
def era(year):
    if year < 1970:
        return "Classic (pre-1970)"
    elif year < 1990:
        return "Golden Age (1970-1989)"
    elif year < 2000:
        return "Modern Era (1990-1999)"
    elif year < 2010:
        return "2000s Expansion"
    else:
        return "Contemporary (2010+)"

enriched["era"] = enriched["year"].apply(era)

# --- Preview ---
print("\nEnriched dataset sample:")
print(enriched[["set_num", "name", "year", "theme_name", "num_parts", "decade_label", "complexity", "era"]].head(10))

print("\nComplexity tier distribution:")
print(enriched["complexity"].value_counts())

# --- Save ---
enriched.to_csv("enriched_sets.csv", index=False)
print("\nEnriched dataset saved: enriched_sets.csv")
print("\n✅ Transform complete!")
print("💡 Question: What other derived columns could be useful for analysis?")
