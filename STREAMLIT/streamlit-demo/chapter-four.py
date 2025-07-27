import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload your CSV File",type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)
    
if file:
    st.subheader("Summary Stats")
    st.write(df.describe())
    
if file:
    cities = df['City'].unique()
    selected_city = st.selectbox("Select a City", cities)
    df_city = df[df['City'] == selected_city]
    st.dataframe(df_city)