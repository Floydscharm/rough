import streamlit as st
from PIL import Image

from pages.home import set_page

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: auto;
        }
        .profile-card {
            background-color: #1E1E1E;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .profile-info {
            display: flex;
            align-items: center;
        }
        .profile-pic {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .match-score {
            color: #32CD32;
            font-weight: bold;
        }
         .bottom-navbar {
        position: responsive;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #09090B;
        padding: 15px 0;
        display: flex;
        justify-content: space-around;
        border-top: 2px solid white;
        z-index: 1000;
    }
    .nav-button {
        font-size: 24px;
        color: white;
        cursor: pointer;
    }
    .nav-button:hover {
        color: #6739b7;
    }
    .center-text {
        text-align: center;
        color: white;
        font-size: 20px;
        margin-top: 80px;
    }
        .profile-icon {
     position: absolute;
     top: 0px;
     right: 15px;
     width: 40px;
     height: 40px;
     border-radius: 50%;
     object-fit: cover;
     border: 2px solid white;
    }
    .hamburger {
         position: absolute;
         top: 0px;
         left: 15px;
         font-size: 28px;
         color: white;
         cursor: pointer;
        }
        .navbar-title {
         font-size: 20px;
         font-weight: bold;
         color: white;
         text-align: center;
         margin-top: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Top Navigation Bar
st.markdown("""
    <div class="hamburger">☰</div>
    <div class="navbar-title">HireMatch</div>
    <img class="profile-icon" src="https://via.placeholder.com/40" alt="Profile">
""", unsafe_allow_html=True)

# Dummy data for profiles
profiles = [
    {"name": "Sneha Chakraborty", "match": "95% match", "desc": "Freshman at Academy of Technology", "connections": "7 mutual connection", "new": "New", "image": "arrow-left.png "},
    {"name": "Atrayee Munshi", "match": "90% match", "desc": "Worked at TCS", "connections": "10 mutual connection", "new": "2 days ago", "image": "top employees.png"},
    {"name": "Anushree Oraon", "match": "90% match", "desc": "Freshman at Academy of Technology", "connections": "2 mutual connection", "new": "2 days ago", "image": "top employees.png"},
]

# Page title
st.markdown("""
    <div class='container'>
        <h2>Top job picks for you</h2>
        <p>Based on comparing resume and job description</p>
    </div>
""", unsafe_allow_html=True)

# Profile listings
for profile in profiles:
    st.markdown(
        f"""
        <div class='profile-card'>
            <div class='profile-info'>
                <img class='profile-pic' src='{profile['image']}'/>
                <div>
                    <b>{profile['name']}</b> <br>
                    <span class='match-score'>{profile['match']}</span><br>
                    {profile['desc']}<br>
                    {profile['connections']}<br>
                    <small>{profile['new']}</small>
                </div>
            </div>
            <span style='color: white;'>❌</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# Fixed Bottom Navbar
st.markdown(
    """
    <div class="bottom-navbar">
        <span class="nav-button" onclick="window.location.href='?page=home'">🏠</span>
        <span class="nav-button" onclick="window.location.href='?page=search'">🔍</span>
        <span class="nav-button" onclick="window.location.href='?page=job'">👜</span>
        <span class="nav-button" onclick="window.location.href='?page=profile'">👤</span>
    </div>
    """,
    unsafe_allow_html=True
)

