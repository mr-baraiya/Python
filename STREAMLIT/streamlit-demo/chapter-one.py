import streamlit as st

st.title("Streamlit Demo")
st.subheader("This is a simple Streamlit application.")

language = st.selectbox(
    "Choose a Programming Language:",
    [
        "Python",
        "JavaScript",
        "Java",
        "C++",
        "C#",
        "Go",
        "Ruby",
        "Swift",
        "Kotlin",
        "Rust"
    ]
)
st.markdown(f"**You selected: {language}**")
st.success(f"Last you chose successfully: {language}")