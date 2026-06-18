"""
STEP 4 — Aggregate & Summarise
================================
The final step of a data pipeline is producing summary tables that
stakeholders and analysts can use to answer business questions.

This step covers:
  - Group-by aggregations
  - Pivot tables
  - Writing final output tables
"""

import pandas as pd

# --- Load enriched data ---
df = pd.read_csv("enriched_sets.csv")
print(f"Loaded enriched sets: {df.shape}")

# --- Summary 1: Sets and parts by decade ---
by_decade = (
    df.groupby("decade_label")
    .agg(
        total_sets=("set_num", "count"),
        total_parts=("num_parts", "sum"),
        avg_parts=("num_parts", "mean"),
        max_parts=("num_parts", "max"),
    )
    .round(1)
    .reset_index()
    .sort_values("decade_label")
)

print("\nSets and parts by decade:")
print(by_decade.to_string(index=False))

# --- Summary 2: Top themes per decade ---
top_themes_per_decade = (
    df.groupby(["decade_label", "theme_name"])
    .size()
    .reset_index(name="set_count")
    .sort_values(["decade_label", "set_count"], ascending=[True, False])
    .groupby("decade_label")
    .head(3)
)

print("\nTop 3 themes per decade:")
print(top_themes_per_decade.to_string(index=False))

# --- Summary 3: Complexity mix over time ---
complexity_pivot = (
    df.groupby(["decade_label", "complexity"])
    .size()
    .unstack(fill_value=0)
    .reset_index()
)

print("\nComplexity distribution by decade:")
print(complexity_pivot.to_string(index=False))

# --- Summary 4: Era summary ---
by_era = (
    df.groupby("era")
    .agg(
        total_sets=("set_num", "count"),
        avg_parts=("num_parts", "mean"),
        pct_expert=("complexity", lambda x: (x == "Expert").mean() * 100),
    )
    .round(1)
    .reset_index()
)

print("\nSummary by era:")
print(by_era.to_string(index=False))

# --- Save output tables ---
by_decade.to_csv("output_by_decade.csv", index=False)
top_themes_per_decade.to_csv("output_top_themes.csv", index=False)
complexity_pivot.to_csv("output_complexity.csv", index=False)
by_era.to_csv("output_by_era.csv", index=False)

print("\nOutput tables saved:")
print("  output_by_decade.csv")
print("  output_top_themes.csv")
print("  output_complexity.csv")
print("  output_by_era.csv")

print("\n✅ Aggregation complete! These tables are ready for dashboards or reports.")
print("💡 Question: Which era saw the biggest jump in set complexity?")
