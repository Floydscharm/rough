import streamlit as st

from pages.home import set_page

# Page Config
st.set_page_config(page_title="HireMatch", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            background-color: #09090B;
        }
        .main-container {
            text-align: center;
            color: white;
            margin-top: 30vh;
            width: 50%;
            margin: 50%
            
        }
        .heading {
            font-size: 30px;
            font-weight: medium;
            text-align: center;
            color: #E4E4E7;
        }
        .upload-btn {
            background-color: #7A40F2;
            color: white;
            font-size: 14px;
            font-weight: bold;
            padding: 12px 25px;
            border-radius: 20px;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            cursor: pointer;
            width: 200px;
            margin-left: 35%;
            margin-top: 10px;
            margin-bottom: 50%;

        }
        .upload-btn:hover {
            background-color: #652DD6;
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
            top: 15px;
            right: 15px;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid white;
        }
        .hamburger {
            position: absolute;
            top: 15px;
            left: 15px;
            font-size: 28px;
            color: white;
            cursor: pointer;
        }
        .navbar-title {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-align: center;
            margin-top: -4px;
        }
    </style>
""", unsafe_allow_html=True)

# Top Navigation Bar
st.markdown("""
    <div class="hamburger">☰</div>
    <div class="navbar-title">HireMatch</div>
    <img class="profile-icon" src="https://via.placeholder.com/40" alt="Profile">
""", unsafe_allow_html=True)

# Main Container
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<p class="heading">Having a tough time selecting which job suits you best?</p>', unsafe_allow_html=True)

# Upload Button
uploaded_file = st.file_uploader("", type=["pdf", "docx"], label_visibility="collapsed")

st.markdown("""
    <button class="upload-btn" mar>
        Upload resume &#128228;
    </button>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

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

# Handling Navbar Clicks with Session State
if "page" in st.experimental_get_query_params():
    selected_page = st.experimental_get_query_params()["page"][0]
    if selected_page in ["home", "search", "job", "profile"]:
        set_page(selected_page)
