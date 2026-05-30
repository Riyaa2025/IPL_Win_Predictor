import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Load model
# -----------------------------
pipe = pickle.load(open('pipe.pkl', 'rb'))

# -----------------------------
# Teams
# -----------------------------
teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

# -----------------------------
# Cities
# -----------------------------
cities = [
    'Hyderabad',
    'Mumbai',
    'Indore',
    'Kolkata',
    'Delhi',
    'Chandigarh',
    'Jaipur',
    'Chennai',
    'Cape Town',
    'Port Elizabeth',
    'Durban',
    'Centurion',
    'East London',
    'Johannesburg',
    'Kimberley',
    'Bloemfontein',
    'Ahmedabad',
    'Cuttack',
    'Nagpur',
    'Dharamsala',
    'Visakhapatnam',
    'Pune',
    'Raipur',
    'Ranchi',
    'Abu Dhabi',
    'Sharjah',
    'Mohali',
    'Bengaluru'
]

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>

    .stApp {
        background-image:
        linear-gradient(
        rgba(255,255,255,0.72),
        rgba(255,255,255,0.72)),
        url("https://crickettimes.com/wp-content/uploads/2020/08/IPL-2020-1.jpg");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .main-header {
        font-size: 4.2em;
        font-weight: 900;
        color: #0D47A1;
        text-align: center;
        margin-bottom: 18px;
        text-shadow: 2px 2px 6px rgba(255,255,255,0.8);
    }

    .subheader {
        font-size: 1.9em;
        font-weight: 800;
        color: #0D47A1;
        margin-top: 25px;
        margin-bottom: 15px;
        border-bottom: 3px solid #1976D2;
        padding-bottom: 8px;
    }

    .prediction-header {
        font-size: 2.8em;
        font-weight: 900;
        color: #0D47A1;
        text-align: center;
        margin-top: 30px;
    }

    .stButton > button {
        background-color: #2E7D32;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 28px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #1B5E20;
    }

    label,
    p,
    div {
        color: #111111 !important;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Title
# -----------------------------
st.markdown(
    '<p class="main-header">IPL Win Predictor 🏏</p>',
    unsafe_allow_html=True
)

# -----------------------------
# Match Details
# -----------------------------
st.markdown(
    '<p class="subheader">Match Details</p>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
        'Select Batting Team',
        sorted(teams)
    )

with col2:
    bowling_team = st.selectbox(
        'Select Bowling Team',
        sorted(teams)
    )

selected_city = st.selectbox(
    'Select Host City',
    sorted(cities)
)

target = st.number_input(
    'Enter Target Score',
    min_value=1,
    value=180
)

# -----------------------------
# Current Match Situation
# -----------------------------
st.markdown(
    '<p class="subheader">Current Match Situation</p>',
    unsafe_allow_html=True
)

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input(
        'Current Score',
        min_value=0
    )

with col4:
    overs = st.number_input(
        'Overs Completed',
        min_value=0.1,
        max_value=20.0,
        step=0.1
    )

with col5:
    wickets = st.number_input(
        'Wickets Out',
        min_value=0,
        max_value=9
    )

# -----------------------------
# Prediction button
# -----------------------------
st.markdown("---")

if st.button("Predict Probability"):

    if batting_team == bowling_team:
        st.error("Batting and bowling teams cannot be the same.")
        st.stop()

    runs_left = max(target - score, 0)

    balls_left = int(120 - (overs * 6))
    balls_left = max(balls_left, 1)

    wickets_remaining = 10 - wickets

    crr = score / overs if overs > 0 else 0

    rrr = (
        (runs_left * 6) / balls_left
        if balls_left > 0
        else 0
    )

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets_remaining],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)

    loss = result[0][0]
    win = result[0][1]

    # -----------------------------
    # Results
    # -----------------------------
    st.markdown(
        '<p class="prediction-header">Prediction</p>',
        unsafe_allow_html=True
    )

    st.success(
        f"{batting_team}: {round(win*100)}% Win Probability"
    )

    st.info(
        f"{bowling_team}: {round(loss*100)}% Win Probability"
    )

    st.markdown("---")

    st.markdown(f"**Runs Left:** {runs_left}")
    st.markdown(f"**Balls Left:** {balls_left}")
    st.markdown(f"**Wickets Remaining:** {wickets_remaining}")
    st.markdown(f"**Current Run Rate:** {crr:.2f}")
    st.markdown(f"**Required Run Rate:** {rrr:.2f}")