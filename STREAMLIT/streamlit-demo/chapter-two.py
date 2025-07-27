import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.title("Age Calculator")

dob = st.date_input(
    "Select your date of birth",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
)

if dob:
    today = date.today()
    diff = relativedelta(today, dob)
    st.markdown(
        f"""
        <div style="background-color:#f0f2f6;padding:20px;border-radius:10px;">
            <h2 style="color:#4F8BF9;">Your Age</h2>
            <p style="font-size:22px; color:#000000;">
                <b>{diff.years}</b> years,
                <b>{diff.months}</b> months,
                <b>{diff.days}</b> days
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
