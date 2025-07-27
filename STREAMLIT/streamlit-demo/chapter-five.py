# chapter-five.py
# This script fetches data from a mock API and displays it in a Streamlit app.
import streamlit as st
import pandas as pd
import requests

api = "https://66724c64e083e62ee43ea0b2.mockapi.io/faculty"

def fetch_data():
    response = requests.get(api)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data from API")
        return []

def display_data(data):
    df = pd.DataFrame(data)
    st.title("Faculty Data")
    st.dataframe(df)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data"])

if page == "Home":
    st.title("Welcome to the Faculty Data App")
    st.write("Use the sidebar to navigate through the app.")
elif page == "Data":
    data = fetch_data()
    if data:
        display_data(data)
        