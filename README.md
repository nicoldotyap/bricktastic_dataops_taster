# Bricktastic DataOps Taster 🧱

Welcome! Today you'll get a hands-on taste of two of the most exciting careers in tech:
**Data Science** and **Data Engineering** — using som play data.

---

## Getting Started

### 1. Open this repo in GitHub Codespaces
- Go to **https://github.com/nicoldotyap/bricktastic_dataops_taster**
- Click the green **Code** button
- Click the **Codespaces** tab
- Click **Create codespace on main**
- Wait ~1 minute for VS Code to load in your browser

### 2. Install Python extension
- Click the **Extensions icon** in the left sidebar (four squares)
- Search for **Python** and install the one by Microsoft

### 3. Install dependencies
Open the terminal (`Ctrl + ~`) and run:
```
pip install -r requirements.txt
```

---

## What's Inside

```
data/                          Raw LEGO data (sets, themes, colors)
data_science/                  Forecasting model — 5 steps
data_engineering/              Data pipeline — 5 steps
```

---

## Track A — Data Science 📊

Data scientists use data to make predictions. You'll build a forecasting model
to predict how many LEGO sets will be released in future years.

Run the scripts **in order**:

| File | What you'll learn |
|------|-------------------|
| `01_explore.py` | Load and visualise the data |
| `02_features.py` | Engineer features (lag, rolling average) |
| `03_train.py` | Train a Linear Regression model |
| `04_evaluate.py` | Measure model accuracy (MAE, R²) |
| `05_challenge.py` | **Your turn** — forecast the next 5 years |

---

## Track B — Data Engineering ⚙️

Data engineers build the pipelines that make data usable. You'll build a
pipeline that ingests, cleans, transforms, and aggregates LEGO data.

Run the scripts **in order**:

| File | What you'll learn |
|------|-------------------|
| `01_ingest.py` | Load raw data and check quality |
| `02_clean.py` | Fix nulls, types, and duplicates |
| `03_transform.py` | Join tables and add derived columns |
| `04_aggregate.py` | Produce summary tables |
| `05_challenge.py` | **Your turn** — analyse LEGO colors |

---

## Suggested Day Schedule

| Time | Activity |
|------|----------|
| 09:00 – 09:30 | Intro + setup (30 min) |
| 09:30 – 11:00 | Track A: Data Science (90 min) |
| 11:00 – 11:15 | Break (15 min) |
| 11:15 – 12:45 | Track B: Data Engineering (90 min) |
| 12:45 – 13:00 | Group debrief + Q&A (15 min) |

**Time per step (each track):**

| Step | Estimated Time |
|------|---------------|
| 01 – 04 (guided steps) | ~45 min total |
| 05 (challenge) | 20–30 min |

Steps 01–04 can run without the challenge if time is short. Step 05 is the extension for fast finishers.

---

## What to Expect — Script by Script

### Track B — Data Engineering

**`01_ingest.py` — Load Raw Data**
You'll load three CSV files — LEGO sets, themes, and colors — using pandas. The script checks each table for basic quality issues: how many rows and columns it has, what data types each column uses, whether any values are missing, and whether any rows are duplicated. It prints a clear summary to the terminal and saves the raw tables as snapshots. Think of this as the data engineer's first look at the data before doing anything with it. You'll see how real-world data is rarely perfect straight out of the box.

**`02_clean.py` — Clean the Data**
Raw data is messy. This script tidies it up before it can be used. It standardises column names, removes sets with invalid or missing years, fills in unknown part counts with zero, and converts data types so everything is consistent. It does the same for themes and colors — trimming whitespace, fixing capitalisation, and standardising boolean values. Cleaned versions of all three tables are saved as new files. You'll learn why data engineers never overwrite raw data and always save a clean copy separately.

**`03_transform.py` — Transform the Data**
This is where the data gets enriched and made useful for analysis. The script joins the sets table with the themes table so each set shows its theme name. It then adds three new columns: a decade label (e.g. "1980s"), a complexity tier based on part count (Simple / Standard / Advanced / Expert), and an era label (e.g. "Golden Age"). You'll see how joining tables and adding derived columns turns flat data into something much more informative and ready for reporting.

**`04_aggregate.py` — Aggregate and Summarise**
The final pipeline step produces summary tables that answer real business questions. The script groups data by decade to show how set counts and part numbers changed over time, finds the top three themes in each decade, breaks down complexity tiers per decade, and summarises each era by average parts and percentage of expert-level sets. Four output CSV files are saved. This is what analysts and stakeholders actually use — not the raw rows, but the summaries built on top of them.

**`05_challenge.py` — Your Turn (Data Engineering)**
This is your open-ended challenge. You'll bring in the colors data and explore how transparent versus non-transparent LEGO colors are distributed. There are `TODO` comments guiding you: load the data, count transparency types, group colors into families (e.g. "Trans", "Dark", "Bright"), and create a chart of your findings. There's no single right answer — the goal is to practise building your own pipeline step from scratch using what you've learned in steps 1 to 4.

---

### Track A — Data Science

**`01_explore.py` — Explore the Data**
Before building any model, data scientists study the data visually. This script loads the LEGO sets and themes tables, prints basic statistics — shape, column types, missing values, year range — and then produces three charts: sets released per year, average parts per set over time, and the top 10 themes by number of sets. The charts are saved as PNG files you can open in VS Code. You'll get a feel for what the data looks like and start noticing trends before any modelling begins.

**`02_features.py` — Feature Engineering**
Models can't learn from raw numbers alone — they need meaningful signals. This script takes the yearly set counts and creates new features: lag values (how many sets were released last year and two years ago), rolling averages over three and five years to smooth out noise, and year-on-year growth percentage. These features give the model a sense of trend and momentum. A chart comparing actual counts versus rolling averages is saved. You'll understand why feature engineering is often where the most important data science work happens.

**`03_train_forecast.py` — Train a Forecasting Model**
This script trains a Linear Regression model to predict how many LEGO sets will be released in a given year. It splits the data 80/20 into training and test sets, keeping time order intact so the model is always predicting forward. After training, it prints the coefficient for each feature — showing how much each one influences the prediction. The trained model is saved as a pickle file for use in the next step. You'll see how machine learning models are built, saved, and handed off in a real workflow.

**`04_evaluate.py` — Evaluate the Model**
A model is only useful if you can measure how good it is. This script loads the saved model and test data, makes predictions, and calculates three metrics: MAE (how many sets off on average), RMSE (which penalises big errors more), and R² (how much of the variation the model explains). It also plots actual versus predicted values so you can see where the model performs well and where it struggles. You'll learn how data scientists decide whether a model is good enough to use and where it might need improvement.

**`05_challenge.py` — Your Turn (Data Science)**
Now you use the trained model to look into the future. Your task is to forecast how many LEGO sets will be released in the next five years. You'll load the model and historical features, build a new DataFrame for future years with estimated lag and rolling values, call `model.predict()`, and plot the historical data alongside your forecast with a dashed line separating past from future. `TODO` comments guide each step. It's the payoff of the whole track — turning everything you've built into an actual prediction.

---

## Tips

- Each script has a **💡 Question** at the end — discuss with the group!
- The **05_challenge.py** files have `TODO` comments where you fill in the code
- Charts are saved as `.png` files — right-click to open them in VS Code
- If something breaks, read the error message — it almost always tells you what's wrong

---

## Data Source

LEGO dataset adapted from the [Rebrickable LEGO Database](https://rebrickable.com/downloads/).
