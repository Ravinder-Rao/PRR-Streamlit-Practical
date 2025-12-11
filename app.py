import streamlit as st

st.set_page_config(page_title="Welcome App", page_icon=":wave:")

st.title("Welcome to Anurag University!")
st.write("A simple welcome Streamlit application.")

st.sidebar.header("About")
st.sidebar.write("Enter your name and press the button to receive a greeting.")

name = st.text_input("What's your name?")

if st.button("Say hello"):
    if name and name.strip():
        st.success(f"Hello, {name.strip()}! Welcome to this Streamlit app. :tada:")
    else:
        st.error("Please enter your name.")

st.write("---")
st.write("Built with Streamlit. Edit `app.py` to customize the app.")
