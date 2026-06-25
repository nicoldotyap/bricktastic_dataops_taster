# Data Science Track — Discussion Question Answers

This file is for facilitators. Share answers after students have had time to discuss each question themselves.

---

## 01_explore.py
**💡 Question: How does this data compare to exploring the raw CSV directly?**

The enriched dataset is significantly more useful than the raw CSV. The raw data only has set number, name, year, theme ID (a number), and part count. The engineered version adds the actual theme name (so you can read "Star Wars" instead of "18"), a complexity tier, a decade label, and an era label — all pre-calculated and joined in. This means a data scientist can start answering real questions immediately, without needing to know how the tables relate to each other. It also means the data has already been validated — nulls filled, types corrected, invalid years removed — so the scientist can trust what they're looking at.

---

## 02_features.py
**💡 Question: Why do we use rolling averages? What does smoothing help with?**

Real-world data is noisy — one unusual year (a big product launch, a supply chain disruption, a global event) can cause a spike or dip that doesn't reflect the underlying trend. A rolling average smooths out that noise by averaging each year with its neighbours, making the long-term trend much easier to see. For a forecasting model, this matters because we want it to learn the trend, not memorise individual bumps. A model trained on raw noisy data might learn "there was a spike in 2007" rather than "LEGO output grows steadily over time" — and that won't generalise to future predictions.

---

## 03_train_forecast.py
**💡 Question: Why do we NOT shuffle the data before splitting for time series?**

Shuffling would let the model "cheat". If we shuffle, the training set might contain data from 2015 and the test set might contain data from 2010. The model would then be trained on future information and tested on the past — which is the opposite of how forecasting works in real life. We always have to predict forward, never backward. Keeping the time order intact (oldest years for training, most recent years for testing) is called a temporal split, and it gives us an honest measure of how well the model would actually perform if we deployed it to predict next year's LEGO releases.

---

## 04_evaluate.py
**💡 Question: Where does the model perform worst? What might cause that?**

The model typically performs worst in years with sudden large changes — for example a sharp spike in new sets released, or an unexpected drop. This happens because Linear Regression assumes the relationship between features and the target is smooth and consistent over time. It cannot anticipate step-changes caused by external factors (a new product line launching, licensing deals like Star Wars being added, economic downturns). The lag and rolling average features help capture momentum, but they always lag behind sudden shifts by definition. A more advanced model (like a gradient boosted tree or an LSTM neural network) could handle these better.

---

## 05_challenge.py
**💡 Question: How accurate do you think your forecast is?**

The honest answer is: reasonably accurate for the near term (1–2 years ahead), less reliable further out. The model extrapolates the trends it learned from historical data, so if LEGO continues growing at a similar pace, the forecast will be close. But it cannot account for future events it has never seen — new licensing deals, economic recessions, major product strategy changes. A good data scientist always communicates uncertainty alongside a forecast, not just the single predicted number. In production, this would typically include a confidence interval showing the range of likely outcomes.

**💡 Bonus: Does using clean engineered data change the forecast vs raw data?**

Yes, subtly. The raw data has missing part counts (filled as blank), inconsistent capitalisation, and no invalid-year filtering. The clean data has those issues resolved — invalid years removed, part counts standardised. Because we're forecasting on yearly set counts (not part counts), the main impact comes from any sets with invalid years being excluded from the clean data. This shifts the yearly aggregates slightly, which flows through to the lag and rolling average features, which in turn affects what the model learns. In general, cleaner input data produces more reliable models — this is why the data engineering pipeline exists.

---

*Facilitator note: encourage students to look at the actual charts their model produced before discussing 04 and 05 — the visual gives a much more concrete starting point for the conversation.*
