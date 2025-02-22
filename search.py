import streamlit as st

# Page Configuration
st.set_page_config(page_title="Search Jobs", layout="wide")

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
    .center-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        width: 100%;
        margin-top: 80px;
    }
    .search-bar {
        display: flex;
        align-items: center;
        background-color: #333333;
        padding: 10px;
        border-radius: 10px;
        width: 50%;
        margin: 20px auto;
    }
    .search-bar input {
        background-color: transparent;
        border: none;
        color: white;
        width: 100%;
        outline: none;
        font-size: 16px;
        padding-left: 10px;
    }
    .search-icon {
        font-size: 20px;
        color: white;
    }
    .filter-widget {
        background-color: #333333;
        padding: 10px;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
        width: 60%;
    }
    .filter-button {
        background-color: rgba(0, 0, 0, 0.2);
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
    }
    .filter-button:hover {
        background-color: #6739b7;
    }
    .section-title {
        color: white;
        font-size: 23px;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        margin-top: 30px;
        text-align: center;
    }
    .horizontal-scroll {
        display: flex;
        overflow-x: auto;
        padding: 10px 0;
        gap: 10px;
        justify-content: center;
    }
    .profile-card {
        display:flex;
        flex-direction:column;
        align-items:centre;
        background-color: black;
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        min-width: 180px;
        max-width: 180px;
        box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
    }
    .connect-btn {
        border: 2px solid #6739b7;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
        margin-top: 10px;
    }
    .connect-btn:hover {
        background-color: #6739b7;
    }
    .bottom-navbar {
        position: fixed;
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
    """,
    unsafe_allow_html=True
)

# Session State for Navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to Update Page
def set_page(page_name):
    st.session_state.page = page_name

# Fixed Top Navbar
st.markdown(
    """
    <div class="top-navbar">
        <span class="menu-icon">☰</span>
        <span style="color:white; font-size:18px;">Search Jobs</span>
        <span class="profile-icon">👤</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Centered Content
st.markdown('<div class="center-content">', unsafe_allow_html=True)

# Search Bar
st.markdown('<div class="search-bar">', unsafe_allow_html=True)
search_query = st.text_input("", placeholder="Search for jobs...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Filter Widget
st.markdown('<div class="filter-widget">', unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6 = st.columns(6)
filters = ["50% Match", "60% Match", "70% Match", "80% Match", "90% Match", "100% Match"]
selected_filter = None

for i, percentage in enumerate(filters):
    if locals()[f"col{i+1}"].button(percentage):
        selected_filter = percentage

st.markdown('</div>', unsafe_allow_html=True)

# "You Might Also Be Interested" Section
st.markdown('<p class="section-title">You Might Also Be Interested</p>', unsafe_allow_html=True)

# Sample Profiles for Horizontal Scrolling
profiles = [
    {"name": "Alice Johnson", "company": "Google", "image": "👩‍💼"},
    {"name": "Bob Smith", "company": "Amazon", "image": "👨‍💼"},
    {"name": "Charlie Brown", "company": "Microsoft", "image": "👨‍💻"},
    {"name": "Diana Ross", "company": "Meta", "image": "👩‍💻"},
    {"name": "Edward Norton", "company": "Tesla", "image": "👨‍🔧"},
]

st.markdown('<div class="horizontal-scroll">', unsafe_allow_html=True)

for profile in profiles:
    with st.container():
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:40px;'>{profile['image']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='profile-name'>{profile['name']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='job-details'>🏢 {profile['company']}</p>", unsafe_allow_html=True)
        connect_key = f"connect_{profile['name'].replace(' ', '_')}"
        if st.button("Connect", key=connect_key):
            st.markdown('<style>.connect-btn { background-color: #6739b7 !important; }</style>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close center content

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
