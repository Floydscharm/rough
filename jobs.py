import streamlit as st

# Configure Streamlit page for mobile-friendly view
st.set_page_config(page_title="My Jobs", layout="centered")

# Custom CSS for styling and responsiveness
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
    }

    body {
        background-color: #0F0F0F;
    }

    .search-container {
        display: flex;
        justify-content: center;
            padding-left: 30px;
        margin-bottom: 20px;
    }

    .search-box {
        width: 80%;
        max-width: 400px;
        height: 40px;
        padding: 20px;
        border-radius: 8px;
        border: none;
        font-size: 16px;
    }

    .search-icon {
        background-color: white;
        padding: 12px;
        border-radius: 8px;
        margin-left: -40px;
        cursor: pointer;
    }

    .job-category {
        display: flex;
        justify-content: center;
        margin-bottom: 15px;
    }

    .job-category button {
        padding: 8px 15px;
        margin: 5px;
        border-radius: 20px;
        border: none;
        cursor: pointer;
        font-size: 14px;
    }

    .active-tab {
        background-color: #A855F7;
        color: white;
    }

    .inactive-tab {
        background-color: transparent;
        border: 1px solid #A855F7;
        color: #A855F7;
    }

    .job-card {
        background-color: #2A2A2A;
        padding: 15px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 10px;
    }

    .job-card img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-right: 10px;
    }

    .job-card div {
        color: white;
        flex-grow: 1;
    }

    .job-card small {
        color: gray;
    }

    .bottom-nav {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #1A1A1A;
        padding: 10px 0;
        display: flex;
        justify-content: space-around;
        border-top: 1px solid #444;
    }

    .bottom-nav button {
        background: transparent;
        border: none;
        color: white;
        font-size: 18px;
        cursor: pointer;
    }

    .active-nav {
        color: #A855F7;
    }
    
    </style>
""", unsafe_allow_html=True)

# State Management for Tabs and Navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "jobs"
if "job_tab" not in st.session_state:
    st.session_state.job_tab = "Applied"

# Function to Switch Pages
def switch_page(page):
    st.session_state.current_page = page

# Function to Switch Job Tabs
def switch_job_tab(tab):
    st.session_state.job_tab = tab

# Search Bar
st.markdown('<div class="search-container">', unsafe_allow_html=True)
search_query = st.text_input("", placeholder="Search", key="search")
st.markdown('<button class="search-icon">🔍</button>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Main Page Content (Dynamic Based on Current Page)
if st.session_state.current_page == "jobs":
    st.markdown("<h4 style='color: white;'>My Jobs</h4>", unsafe_allow_html=True)

    # Job Category Tabs
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Applied", key="applied", help="Applied Jobs", on_click=switch_job_tab, args=("Applied",)):
            st.session_state.job_tab = "Applied"
    with col2:
        if st.button("Pending", key="pending", help="Pending Jobs", on_click=switch_job_tab, args=("Pending",)):
            st.session_state.job_tab = "Pending"
    with col3:
        if st.button("Offered", key="offered", help="Offered Jobs", on_click=switch_job_tab, args=("Offered",)):
            st.session_state.job_tab = "Offered"

    # Job Listings Based on Selected Tab
    jobs = {
        "Applied": [
            {"name": "Tesla", "location": "Los Angeles, CA", "logo": "https://via.placeholder.com/40"},
            {"name": "TCS", "location": "Kolkata, India", "logo": "https://via.placeholder.com/40"}
        ],
        "Pending": [
            {"name": "Amazon", "location": "Seattle, WA", "logo": "https://via.placeholder.com/40"}
        ],
        "Offered": [
            {"name": "Google", "location": "Mountain View, CA", "logo": "https://via.placeholder.com/40"}
        ]
    }

    for job in jobs.get(st.session_state.job_tab, []):
        st.markdown(f"""
        <div class="job-card">
            <img src="{job['logo']}">
            <div>
                <strong>{job['name']}</strong><br>
                <small>{job['location']}</small>
            </div>
            <span style="color: white; font-size: 18px;">➝</span>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_page == "home":
    st.markdown("<h4 style='color: white;'>Home Page</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: white;'>Welcome to the Home Page!</p>", unsafe_allow_html=True)

elif st.session_state.current_page == "search":
    st.markdown("<h4 style='color: white;'>Search Page</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: white;'>Search for jobs and connections here.</p>", unsafe_allow_html=True)

elif st.session_state.current_page == "profile":
    st.markdown("<h4 style='color: white;'>Profile Page</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: white;'>View and edit your profile here.</p>", unsafe_allow_html=True)

# Bottom Navigation Bar
st.markdown("""
    <div class="bottom-nav">
        <button class="{home}" onclick="window.location.reload();">🏠</button>
        <button class="{search}" onclick="window.location.reload();">🔍</button>
        <button class="{jobs}" onclick="window.location.reload();">💼</button>
        <button class="{profile}" onclick="window.location.reload();">👤</button>
    </div>
""".format(
    home="active-nav" if st.session_state.current_page == "home" else "",
    search="active-nav" if st.session_state.current_page == "search" else "",
    jobs="active-nav" if st.session_state.current_page == "jobs" else "",
    profile="active-nav" if st.session_state.current_page == "profile" else ""
), unsafe_allow_html=True)
