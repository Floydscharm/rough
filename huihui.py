import streamlit as st

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to switch pages
def go_to_search():
    st.session_state.page = "search"

def go_to_home():
    st.session_state.page = "home"

# Navigation Buttons
st.sidebar.button("Home", on_click=go_to_home)
st.sidebar.button("Search", on_click=go_to_search)

# Page Content
if st.session_state.page == "home":
    st.title("🏠 Home Page")
    st.write("Welcome to the home page!")
    if st.button("Go to Search"):
        go_to_search()

elif st.session_state.page == "search":
    st.title("🔍 Search Page")
    st.write("You are now on the search page.")
    if st.button("Go to Home"):
        go_to_home()