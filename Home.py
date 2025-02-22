# app.py
import streamlit as st

st.title("Welcome to Our Application")

st.write("This is the main page of our application. Please navigate to the 'Login' page to access your profile.")

st.write("Or you can enter your username and phone number here:")

username = st.text_input("Username", placeholder="Username")
phone = st.text_input("Phone number", placeholder="Phone number")

if st.button("My resume"):
    # Placeholder for resume logic
    if username == "Sneha Chakraborty" and phone == "9432914547":
        st.write("Displaying Sneha Chakraborty's resume...")
    else:
        st.write("Please enter the correct information.")

if st.button("Edit"):
    # Placeholder for edit logic
    if username == "Sneha Chakraborty" and phone == "9432914547":
        st.write("Editing Sneha Chakraborty's profile...")
    else:
        st.write("Please enter the correct information.")

st.write("Navigate to the Login page in the sidebar for a more detailed profile.")