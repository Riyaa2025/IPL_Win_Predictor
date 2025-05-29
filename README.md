# 🏏 IPL Win Probability Predictor

This project predicts the probability of a team winning an IPL match based on current match conditions like runs, wickets, overs left, and target score.

## 🚀 Features
- Built using Logistic Regression on cleaned IPL ball-by-ball data
- Feature engineering includes run rate, required rate, wickets, etc.
- Interactive UI built using Streamlit (runs locally)

## 📂 Files

- `IPL_Win_Commented.ipynb` → Full Jupyter notebook with data analysis, feature engineering, and model training  
- `app.py` → Streamlit app to simulate IPL match scenarios and predict win probabilities  
- `matches.csv` → Match-level IPL dataset used for preprocessing and context  
- `deliveries.csv` → Ball-by-ball delivery dataset used to engineer features like runs, balls remaining, and wickets

## 🛠 Tech Stack
Python, pandas, scikit-learn, Streamlit, matplotlib
