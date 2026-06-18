"""
STEP 5 — YOUR CHALLENGE 🏆
============================
You've ingested, cleaned, transformed, and aggregated LEGO data.
Now it's your turn to build your own pipeline step!

YOUR TASK:
  Bring in the colors data and answer this question:
  "How has the use of transparent vs non-transparent pieces changed over time?"

HINTS:
  - Load clean_sets.csv and ../data/lego_colors.csv
  - The lego_sets data doesn't directly link to colors — think about what
    proxy you could use (e.g. does num_parts correlate with color variety?)
  - Alternatively: analyse the colors table on its own —
    how many transparent vs non-transparent colors exist per color family?
  - Group, aggregate, and produce at least one summary table
  - Plot your findings

This is open-ended — there's no single right answer. Be creative! 🎨
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- Load data ---
# TODO: load clean_sets.csv and ../data/lego_colors.csv
sets   = None  # replace this line
colors = None  # replace this line


# --- Explore colors ---
# TODO: print the shape and first few rows of the colors table
print("Colors shape:", )
print(colors.head())


# --- Analyse transparency ---
# TODO: count how many colors are transparent vs not
transparency_counts = None  # replace this line
print("\nTransparent vs non-transparent colors:")
print(transparency_counts)


# --- Go deeper: color families ---
# HINT: you can extract the first word of the color name as the "family"
# e.g. "Trans-Red" → "Trans", "Dark Blue" → "Dark", "Bright Green" → "Bright"
# colors["family"] = colors["name"].str.split().str[0]

# TODO: group by family and count colors
color_families = None  # replace this line
print("\nColor families:")
print(color_families)


# --- Plot ---
# TODO: create a bar chart or pie chart of your findings
plt.figure(figsize=(10, 5))

# your plot here

plt.title("LEGO Color Analysis")
plt.tight_layout()
plt.savefig("chart_colors.png")
plt.show()


# --- Save a summary table ---
# TODO: save your most interesting summary as output_colors.csv


print("\n🏆 Challenge complete! What did you discover about LEGO colors?")
