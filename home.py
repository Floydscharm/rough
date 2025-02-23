import streamlit as st
# Page Configuration
st.set_page_config(page_title="Job Finder", layout="centered")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    body {
        background-color: #09090B;
    }
    .top-navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
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
    .upload-btn {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .job-card {
        
        background-color: #333333;
        padding: 15px;
        border-radius: 10px;
        color: white;
        box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.1);
        margin-bottom: 10px;
    }
    .job-title {
        font-size: 25px;
        font-weight: bold;
        color:#f4f4f4
    }
    .job-details {
        font-size: 14px;
        color: #BBBBBB;
    }
    .apply-btn {
        background-color: white;
        color: black;
        padding: 5px 10px;
        border-radius: 5px;
        cursor: pointer;
    }
    .apply-btn:hover {
        background-color: #6739b7;
        color: white;
    }
    
/* ...existing code... */

/* Add these new styles */
.stSidebar {
    width: 10px !important;  /* Reduces the sidebar width */
}

.stSidebar [data-testid="stSidebarNav"] {
    min-width: unset !important;
    width: auto !important;
    margin-right: 0 !important;
}

/* Reduce the sash (draggable area) width */
.resize-sensor {
    width: 50px !important;  /* Makes the draggable area thinner */
}

/* Reduce padding between sidebar and main content */
.main .block-container {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 95% !important;
}

/* ...existing code... */

    </style>
    """,
    unsafe_allow_html=True
)

# Session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to update page
def set_page(page_name):
    st.session_state.page = page_name

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

# Scrollable Content
st.write("<br><br><br>", unsafe_allow_html=True)  # Space for navbar

st.markdown('<h class="center-text" style="font-size:25px;text-align:centre;font-weight:medium">Having a tough time selecting which job suits you best?</h>', unsafe_allow_html=True)

# Resume Upload Button
st.markdown('<div class="upload-btn">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Job Section Header
st.write("<br>", unsafe_allow_html=True)
st.markdown('<p class="center-text" style="font-size:22px; font-weight:bold;">Top Job Picks for Today</p>', unsafe_allow_html=True)

# Sample Job Listings
jobs = [
    {"company": "Google", "logo": "🟢", "location": "California, USA", "salary": "$120,000/yr", "type": ["Full Time", "Remote"]},
    {"company": "Microsoft", "logo": "🟢", "location": "Washington, USA", "salary": "$110,000/yr", "type": ["Full Time"]},
    {"company": "Amazon", "logo": "🟠", "location": "Seattle, USA", "salary": "$100,000/yr", "type": ["Remote"]},
    {"company": "Tesla", "logo": "🔴", "location": "Texas, USA", "salary": "$130,000/yr", "type": ["Full Time", "Remote"]},
    {"company": "Facebook", "logo": "🔵", "location": "Menlo Park, USA", "salary": "$115,000/yr", "type": ["Full Time"]},
]

# Display Job Cards
for job in jobs:
    with st.container():
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.markdown(f"<p class='job-title'>{job['logo']} {job['company']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='job-details'>📍 {job['location']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='job-details'>💰 {job['salary']}</p>", unsafe_allow_html=True)

        # Job Type Buttons
        cols = st.columns(len(job["type"]) + 1)
        for i, job_type in enumerate(job["type"]):
            cols[i].button(job_type, key=f"{job['company']}-{job_type}", disabled=True)

        # Job Description Button
        if cols[-1].button("Job Description", key=f"{job['company']}-desc"):
            st.markdown('<style>.apply-btn { background-color: #6739b7 !important; color: white !important; }</style>', unsafe_allow_html=True)

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
if "page" in st.experimental_get_query_params():
    selected_page = st.experimental_get_query_params()["page"][0]
    if selected_page in ["home", "search", "job", "profile"]:
        set_page(selected_page)

