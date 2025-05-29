import streamlit as st
import pickle
import pandas as pd

# Load the model
pipe = pickle.load(open('pipe.pkl','rb'))

# Define teams and cities
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

# --- Custom CSS for Styling with Background Image and Overlay ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)), url("https://crickettimes.com/wp-content/uploads/2020/08/IPL-2020-1.jpg");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed; /* Makes the background image fixed while scrolling */
        color: #000000; /* Default text color set to black for darkest text */
    }}
    .main-header {{
        font-size: 5.0em; /* EVEN LARGER font size for "IPL Win Predictor" */
        font-weight: 900; /* Extra bold */
        color: #00008B; /* Darker blue */
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 4px 4px 8px rgba(0,0,0,0.4); /* Stronger text shadow */
        padding-top: 20px; /* Add some space from the top */
    }}
    .subheader {{
        font-size: 2.2em; /* Slightly larger subheader */
        font-weight: 800; /* More bold */
        color: #1A237E; /* Very dark blue */
        margin-top: 30px;
        margin-bottom: 15px;
        border-bottom: 4px solid #1976D2; /* Thicker, dark blue border */
        padding-bottom: 10px; /* More padding */
    }}
    .stButton>button {{
        background-color: #006400; /* Very dark green for predict button */
        color: white;
        font-weight: bold;
        padding: 16px 35px; /* Even larger padding */
        border-radius: 15px; /* More rounded corners */
        border: none;
        box-shadow: 5px 5px 10px rgba(0,0,0,0.5); /* Strongest shadow */
        transition: all 0.3s ease-in-out;
        cursor: pointer;
    }}
    .stButton>button:hover {{
        background-color: #004d00; /* Even darker green on hover */
        transform: translateY(-4px); /* More pronounced lift */
        box-shadow: 6px 6px 12px rgba(0,0,0,0.6);
    }}
    .stSelectbox, .stNumberInput {{
        background-color: rgba(255, 255, 255, 1.0); /* Fully opaque white for inputs */
        border-radius: 12px; /* More rounded corners */
        padding: 8px 15px;
        box-shadow: 3px 3px 6px rgba(0,0,0,0.3); /* Stronger shadow */
        border: 2px solid #2196F3; /* Darker blue border */
    }}
    label.css-1fv8ic {{ /* Targeting default Streamlit label color */
        color: #1A237E !important; /* Dark blue for labels, important to override */
        font-weight: bold !important; /* Make labels bold, important to override */
        font-size: 1.2em; /* Larger label font */
    }}
    .prediction-header {{
        font-size: 3.5em; /* Even larger prediction header */
        font-weight: 900; /* Extra bold */
        color: #00008B; /* Darker blue for results header */
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 4px solid #42A5F5; /* Thicker border */
        text-shadow: 3px 3px 6px rgba(0,0,0,0.2);
    }}
    .stSuccess, .stInfo {{
        border-radius: 15px; /* More rounded corners */
        padding: 25px; /* More padding */
        margin-top: 25px; /* More margin */
        text-align: center;
        font-size: 2.2em; /* Much larger font for results */
        font-weight: 900; /* Extra bold */
        color: #000000 !important; /* Black text for results */
        background-color: rgba(180, 220, 180, 0.95) !important; /* Darker success background */
        border: 3px solid #006400; /* Dark green border for success */
    }}
    .stInfo {{
        background-color: rgba(170, 200, 240, 0.95) !important; /* Darker info background */
        border: 3px solid #1976D2; /* Dark blue border for info */
    }}
    /* Custom style for general text within the app (outside inputs/buttons) */
    div[data-testid="stVerticalBlock"] > div > div > div > div:not(.stSelectbox) > div:not(.stNumberInput) > p {{
        color: #000000; /* Black for regular text */
        font-weight: bold; /* Make it bold */
    }}
    .stMarkdown p {{
        color: #000000; /* Black for all markdown paragraph text */
        font-weight: bold; /* Make it bold */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- App Title (Now part of the main header styling) ---
st.markdown('<p class="main-header">IPL Win Predictor</p>', unsafe_allow_html=True)

# --- Match Details Section ---
st.markdown('<p class="subheader">Match Details</p>', unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox('Select the **Batting Team**', sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select the **Bowling Team**', sorted(teams))

    selected_city = st.selectbox('Select the **Host City**', sorted(cities))
    target = st.number_input('Enter the **Target Score**', min_value=1, value=180)

# --- Current Match Situation Section ---
st.markdown('<p class="subheader">Current Match Situation</p>', unsafe_allow_html=True)
with st.container():
    col3, col4, col5 = st.columns(3)
    with col3:
        score = st.number_input('Current **Score**', min_value=0)
    with col4:
        overs = st.number_input('**Overs** Completed', min_value=0.0, max_value=20.0, step=0.1)
    with col5:
        wickets = st.number_input('**Wickets** Out', min_value=0, max_value=10)

# --- Prediction Button ---
st.markdown("---") # A horizontal line for separation
if st.button('Predict Probability'):
    # Basic validation for overs
    if overs == 0:
        st.warning("Overs completed cannot be zero for accurate CRR calculation.")
        st.stop() # Stop execution if validation fails
    if batting_team == bowling_team:
        st.error("Batting and Bowling teams cannot be the same!")
        st.stop()

    runs_left = target - score
    balls_left = 120 - (overs * 6)
    current_wickets = 10 - wickets # Inverting for the model's expected format (wickets remaining)

    # Handle edge cases for calculations
    if balls_left <= 0:
        balls_left = 1 # Prevent division by zero; treat as 1 if 0 or negative
        rrr = 0 # If no balls left, RRR is irrelevant or 0 if target met/exceeded
    else:
        rrr = (runs_left * 6) / balls_left

    crr = score / overs if overs > 0 else 0 # Prevent division by zero if overs is 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [current_wickets], # Using current_wickets (wickets remaining)
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    st.markdown('<p class="prediction-header">Prediction:</p>', unsafe_allow_html=True)
    st.success(f"**{batting_team}: {round(win*100)}% Win Probability**")
    st.info(f"**{bowling_team}: {round(loss*100)}% Win Probability**")

    # Optional: Display more detailed stats for user
    st.markdown("---")
    st.markdown(f"<p style='color:#000000; font-weight:900; font-size:1.4em;'>Runs Left: <span style='color:#00008B;'>{runs_left}</span></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#000000; font-weight:900; font-size:1.4em;'>Balls Left: <span style='color:#00008B;'>{balls_left}</span></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#000000; font-weight:900; font-size:1.4em;'>Current Run Rate (CRR): <span style='color:#00008B;'>{crr:.2f}</span></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#000000; font-weight:900; font-size:1.4em;'>Required Run Rate (RRR): <span style='color:#00008B;'>{rrr:.2f}</span></p>", unsafe_allow_html=True)