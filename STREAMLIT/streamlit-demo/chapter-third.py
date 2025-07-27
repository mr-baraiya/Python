import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/4974543/pexels-photo-4974543.jpeg", width=200)
    vote1 = st.button("Vote for Masala Chai")

with col2:
    st.header("Ginger Chai")
    st.image("https://images.pexels.com/photos/905485/pexels-photo-905485.jpeg", width=200)
    vote2 = st.button("Vote for Ginger Chai")
    
if vote1:
    st.success("You voted for Masala Chai!")
if vote2:
    st.success("You voted for Ginger Chai!")
    
name = st.sidebar.text_input("Enter your name:")
tea = st.sidebar.selectbox("Select your favorite tea:", ["Masala Chai", "Ginger Chai", "Other"])

st.sidebar.write(f"Hello {name}, you selected {tea} as your favorite tea!")

with st.expander("About this Poll"):
    st.markdown("### Chai Definition")
    st.write("""
    Chai is a popular beverage in many countries, especially in India. It is made by brewing tea leaves with a mixture of spices, milk, and sugar. There are many variations of chai, each with its unique flavor profile.
    - **Masala Chai**: This version includes a blend of spices such as cardamom, cinnamon, and ginger, giving it a rich and aromatic flavor.
    - **Ginger Chai**: Made with fresh ginger, this chai is known for its zesty and invigorating taste.
    """)
