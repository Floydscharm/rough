import streamlit as st

from pages.home import set_page

# Set Page Config for better responsiveness
st.set_page_config(page_title="Search", layout="centered")

# Custom CSS for styling and responsiveness
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    body {
        background-color: #09090b;
        font-family: 'Poppins', sans-serif;
    }

    /* Centering and styling the search bar */
    .search-container {
    display: flex;
    align-items: center;
    gap: 10px;
    width: 100%;
    margin-bottom: 15px;
}

.search-input {
    flex: 1;
}

.search-button {
    background: none;
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
    padding: 5px 10px;
}

    /* Responsive Filters */
    .filters {
        background-color: #3E3E3E;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
    }

    .filter-button {
        background-color: #5A5A5A;
        border: none;
        padding: 10px 20px;
        border-radius: 6px;
        font-size: 14px;
        margin: 5px;
        color: white;
        cursor: pointer;
        width: 100%;
    }

    /* Profile Card */
    .profile-card {
        background-color: #1A1A1A;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 15px;
        width: 100%;
    }

    .profile-img {
        border-radius: 50%;
        width: 70px;
        height: 70px;
        margin-bottom: 10px;
    }

    .connect-btn {
        background-color: transparent;
        border: 1px solid #A855F7;
        color: #A855F7;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 14px;
        cursor: pointer;
        margin-top: 10px;
    }
        .connect-btn:hover {
        background-color: #A855F7;
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
    

    /* Responsive layout */
    @media (max-width: 768px) {
        .search-box {
            width: 90%;
        }
        .filter-button {
            font-size: 12px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Search Bar
col1, col2 = st.columns([8, 1])
with col1:
    search_query = st.text_input("", placeholder="Search", key="search", label_visibility="collapsed")
with col2:
    st.markdown('<button class="search-button">🔍</button>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Filters Section
st.markdown('<div class="filters">', unsafe_allow_html=True)
st.markdown("<h4 style='color: white;'>Filters</h4>", unsafe_allow_html=True)

# Responsive Filter Layout
filter_cols = st.columns([1, 1, 1])
filter_labels = ["50%", "60%", "70%", "80%", "90%", "100%"]

for i, label in enumerate(filter_labels):
    with filter_cols[i % 3]:  # Distribute buttons across columns
        st.button(label, key=f"filter_{label}")

st.markdown('</div>', unsafe_allow_html=True)

# "You might also be interested" Section
st.markdown("<h4 style='color: white;'>You might also be interested</h4>", unsafe_allow_html=True)

# Profile Data
profiles = [
    {"name": "Sneha Chakraborty", "job": "Works at TGM", "image": "https://via.placeholder.com/70"},
    {"name": "Atrayee Munshi", "job": "Works at TGM", "image": "https://via.placeholder.com/70"},
    {"name": "Anusha Sharma", "job": "Works at TGM", "image": "https://via.placeholder.com/70"}
]

# Mobile-friendly profile layout
profile_cols = st.columns(len(profiles)) if st.session_state.get("device") != "mobile" else st.columns(1)

for col, profile in zip(profile_cols, profiles):
    with col:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.image(profile["image"], width=70)
        st.markdown(f"<p style='color: white;'>{profile['name']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: gray;'>{profile['job']}</p>", unsafe_allow_html=True)
        st.markdown('<button class="connect-btn">Connect</button>', unsafe_allow_html=True)
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
