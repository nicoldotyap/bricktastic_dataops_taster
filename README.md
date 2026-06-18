# Bricktastic DataOps Taster 🧱

Welcome! Today you'll get a hands-on taste of two of the most exciting careers in tech:
**Data Science** and **Data Engineering** — using real LEGO data.

---

## Getting Started

### 1. Open this repo in your browser
Go to **https://vscode.dev** and open this repository.

### 2. Install Python extension
When prompted, install the **Python** extension. VS Code will recommend it automatically.

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

## Tips

- Each script has a **💡 Question** at the end — discuss with the group!
- The **05_challenge.py** files have `TODO` comments where you fill in the code
- Charts are saved as `.png` files — right-click to open them in VS Code
- If something breaks, read the error message — it almost always tells you what's wrong

---

## Data Source

LEGO dataset adapted from the [Rebrickable LEGO Database](https://rebrickable.com/downloads/).
