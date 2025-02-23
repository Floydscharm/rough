import streamlit as st

from pages.home import set_page

# Set page configuration for mobile responsiveness
st.set_page_config(page_title="Job Matches", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
    }

    body {
        background-color: #0F0F0F;
    }

    .container {
        padding: 10px;
        color: white;
    }

    .title {
        text-align: center;
        font-size: 150px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 14px;
        color: gray;
        margin-bottom: 20px;
        overflow-x: -20px;
    }

    .job-card {
        background-color: #333333;
        padding: 15px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 10px;
    }

    .job-card img {
        width: 40px;
        height: 40px;
        border-radius: 5px;
        margin-right: 10px;
    }

    .job-details {
        flex-grow: 1;
    }

    .job-title {
        font-size: 16px;
        font-weight: bold;
        color: white;
    }

    .company {
        font-size: 14px;
        color: #A0A0A0;
    }

    .match-score {
        font-size: 14px;
        font-weight: bold;
        color: #5AF38E;
    }

    .remove-btn {
        background-color: transparent;
        border: none;
        color: white;
        font-size: 18px;
        cursor: pointer;
    }

    .scrollable-container {
        overflow-y: auto;
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
    </style>
""", unsafe_allow_html=True)

# State Management for Navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "job_matches"

# Function to switch pages
def switch_page(page):
    st.session_state.current_page = page

# Header Section
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<h3 class="title">Top job picks for you</h3>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Based on matching your resume</p>', unsafe_allow_html=True)

# Job List Data
jobs = [
    {"title": "UI/UX Designer", "company": "Tesla", "location": "Los Angeles, CA (On-site)", "match": "95%", "logo": "https://via.placeholder.com/40"},
    {"title": "Web Development", "company": "Wipro", "location": "Bengaluru East, Karnataka (Remote)", "match": "90%", "logo": "https://via.placeholder.com/40"},
    {"title": "App Development", "company": "Uplers", "location": "India (Remote)", "match": "90%", "logo": "https://via.placeholder.com/40"},
    {"title": "UI Frontend Developer", "company": "Uplers", "location": "India (Remote)", "match": "85%", "logo": "https://via.placeholder.com/40"},
    {"title": "App Development", "company": "Uplers", "location": "India (Remote)", "match": "82%", "logo": "https://via.placeholder.com/40"},
    {"title": "C++ Developer", "company": "EPAM Systems", "location": "India (Remote)", "match": "80%", "logo": "https://via.placeholder.com/40"},
    {"title": "Data Science", "company": "Uplers", "location": "India (Remote)", "match": "79%", "logo": "https://via.placeholder.com/40"},
    {"title": "Web Development", "company": "Uplers", "location": "India (Remote)", "match": "72%", "logo": "https://via.placeholder.com/40"},
    {"title": "App Development", "company": "Uplers", "location": "India (Remote)", "match": "70%", "logo": "https://via.placeholder.com/40"}
]

# Scrollable Job Listings
st.markdown('<div class="scrollable-container">', unsafe_allow_html=True)
for job in jobs:
    st.markdown(f"""
    <div class="job-card">
        <img src="{job['logo']}">
        <div class="job-details">
            <div class="job-title">{job['title']}</div>
            <div class="company">{job['company']}</div>
            <div class="company">{job['location']}</div>
        </div>
        <div class="match-score">{job['match']} match</div>
        <button class="remove-btn">✖</button>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

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
# if "page" in st.experimental_get_query_params():
#     selected_page = st.experimental_get_query_params()["page"][0]
#     if selected_page in ["home", "search", "job", "profile"]:
#         set_page(selected_page)
