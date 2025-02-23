import streamlit as st

# Set page configuration
st.set_page_config(page_title="Job Finder", layout="centered")

# Session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to update page
def set_page(page_name):
    st.session_state.page = page_name

# Custom CSS for styling
st.markdown("""
    <style>
            
    .center-text {
        text-align: center;
        color: white;
        font-size: 20px;
        margin-top: 80px;
    }
    
    .upload-btn {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
            
    .job-card {
        display: flex;
        align-items: center;
        padding: 15px;
        border-radius: 10px;
        background-color: #f9f9f9;
        margin-bottom: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .job-type-btn {
        background-color: #6739b7;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 5px 10px;
        margin: 2px;
        font-size: 12px;
    }
        .top-navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #09090B;
        padding: 10px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid white;
        z-index: 1000;
    }
    .top-navbar .menu-icon, .top-navbar .profile-icon {
        font-size: 24px;
        color: white;
        cursor: pointer;
    }
        .container {
        min-height: 100vh;
        position: relative;
        padding-bottom: 70px; /* Height of the navbar plus some padding */
    }

    .bottom-navbar {
        position: absolute; /* Change from fixed to absolute */
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
    .container {
        min-height: 100vh;
        position: relative;
        padding-bottom: 60px; /* Reduced padding */
        display: flex;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html=True)

# Fixed Top Navbar
st.markdown(
    """
    <div class="top-navbar">
        <span class="menu-icon">☰</span>
        <span style="color:white; font-size:18px;">Job Finder</span>
        <span class="profile-icon">👤</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("<br><br><br>", unsafe_allow_html=True)  # Space for navbar

st.markdown('<p class="center-text">Having a tough time selecting which job suits you best?</p>', unsafe_allow_html=True)

# Resume Upload Button
st.markdown('<div class="upload-btn">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Job Section Header
st.write("<br>", unsafe_allow_html=True)
st.markdown('<p class="center-text" style="font-size:22px; font-weight:bold;">Top Job Picks for Today</p>', unsafe_allow_html=True)

# Job List Data
jobs = [
    {"company": "Google", "logo": "pics/google.png", "location": "California, USA", "salary": "$120,000/yr", "type": ["Full Time", "Remote"]},
    {"company": "Microsoft", "logo": "pics/microsoft.png", "location": "Washington, USA", "salary": "$110,000/yr", "type": ["Full Time"]},
    {"company": "Amazon", "logo": "pics/amazon.png", "location": "Seattle, USA", "salary": "$100,000/yr", "type": ["Remote"]},
    {"company": "Tesla", "logo": "pics/tesla.png", "location": "Texas, USA", "salary": "$130,000/yr", "type": ["Full Time", "Remote"]},
    {"company": "Facebook", "logo": "pics/facebook.png", "location": "Menlo Park, USA", "salary": "$115,000/yr", "type": ["Full Time"]}
]

# Display Job Cards
for job in jobs:
    # Create columns for the job card layout
    col1, col2, col3 = st.columns([1, 3, 2])

    # Column 1: Company Logo
    with col1:
        try:
            st.image(job["logo"], width=50)  # Adjust width as needed
        except FileNotFoundError:
            st.error(f"Image not found: {job['logo']}")

    # Column 2: Job Details
    with col2:
        st.markdown(f"**{job['company']}**")
        st.markdown(f"📍 {job['location']}")
        st.markdown(f"💰 {job['salary']}")

    # Column 3: Job Type Buttons
    with col3:
        for job_type in job["type"]:
            st.button(job_type, key=f"{job['company']}-{job_type}", disabled=True)

    # Add a divider between job cards
    st.markdown("---")
st.markdown(
    """
    <div class="container">
    <div class="bottom-navbar">
        <span class="nav-button" onclick="window.location.href='?page=home'">🏠</span>
        <span class="nav-button" onclick="window.location.href='?page=search'">🔍</span>
        <span class="nav-button" onclick="window.location.href='?page=job'">👜</span>
        <span class="nav-button" onclick="window.location.href='?page=profile'">👤</span>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)