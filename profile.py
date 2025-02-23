import streamlit as st

from pages.home import set_page

# Page Config
st.set_page_config(page_title="Profile", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #09090B;
        }
        .profile-container {
            text-align: center;
            position: relative;
        }
        .profile-pic {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid white;
            position: absolute;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        .card {
            background-color: #333333;
            padding:  80px;
            border-radius: 15px;
            color: white;
            margin-top: 60px;
        }
        .stTextInput>div>div>input {
            background-color: white !important;
            color: black !important;
            border-radius: 10px;
            text-align: left;
        }
        .resume-box {
            background-color: white;
            height: 150px;
            width: 100%;
            border-radius: 10px;
            padding: 10px;
            overflow-y: auto;
        }
        .edit-text {
            display: flex;
            justify-content: space-between;
            align-items: center;
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
        .nav-icon {
            font-size: 22px;
            color: white;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Profile Section
st.markdown('<div class="profile-container">', unsafe_allow_html=True)
st.image("https://via.placeholder.com/120", caption="", use_column_width=False, width=120, output_format="PNG", channels="RGB", clamp=True)
st.markdown("</div>", unsafe_allow_html=True)

# Profile Info Card
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    username = st.text_input("Username", "Sneha Chakraborty", key="username")
    phone_number = st.text_input("Phone number", "9432914547", key="phone")

    st.markdown('<div class="edit-text"><p>My resume</p> <p style="color:#6739B7; cursor:pointer;">Edit ✏️</p></div>', unsafe_allow_html=True)

    resume = st.file_uploader("", type=["pdf", "docx", "txt"])
    
    if resume:
        st.markdown('<div class="resume-box">📄 Resume uploaded successfully</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="resume-box"></div>', unsafe_allow_html=True)
    
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

