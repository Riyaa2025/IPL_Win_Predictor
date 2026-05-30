# 🏏 IPL Win Probability Predictor

An end-to-end Machine Learning project that predicts the **real-time win probability of IPL matches during a run chase** using historical ball-by-ball IPL data.

Built with **Python, Scikit-learn, and Streamlit**, the model analyzes live match situations based on teams, score, overs, wickets, and venue to estimate winning probability for both teams.

## 🚀 Highlights

* Real-time IPL win probability prediction
* Interactive Streamlit web app
* Trained on historical IPL ball-by-ball data (**2008–2019**)
* Compared multiple ML models:

  * **Logistic Regression → 79.85%**
  * **Random Forest → 83.74%**
* Final model selected based on performance

## 🔍 Data Handling

Carefully cleaned and preprocessed IPL datasets:

* `matches.csv`
* `deliveries.csv`

To improve model reliability:

* Handled missing values
* Standardized team and city names
* Engineered match-state features:

  * Current Run Rate (**CRR**)
  * Required Run Rate (**RRR**)
  * Balls Left
  * Wickets Remaining

### ⚠️ Data Leakage Discovery

A naive random train-test split on ball-by-ball data initially gave **~99% accuracy**, because rows from the same match leaked into both training and test sets.

This was fixed by splitting data using **temporal order (`shuffle=False`)**, bringing performance down to a more realistic and reliable **~80–83%**.

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
