import streamlit as st
import pandas as pd
import datetime
import csv
import os

MOOD_FILE = "mood_log.csv"

# Function to load mood data
def load_mood_data():
    #check if file edxist

    if os.path.exists(MOOD_FILE):
        return pd.read_csv(MOOD_FILE)
    return pd.DataFrame(columns=["Date", "Mood"])

# Function to save mood data
def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)
    
    with open(MOOD_FILE, 'a') as file:
        writer = csv.writer(file)

        # Add header only if file is empty
        if not file_exists or os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])

        writer.writerow([date, mood])

st.title("Mood Tracker")

today = datetime.date.today()
st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood logged successfully")

# Load mood data
data = load_mood_data()

# Display mood trends if data is available
if not data.empty:
    st.subheader("Mood Trends Over Time")

    data["Date"] = pd.to_datetime(data["Date"])

    # Mood-wise count
    mood_counts = data["Mood"].value_counts()
    st.bar_chart(mood_counts)
  


