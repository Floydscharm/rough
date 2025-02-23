import streamlit as st

from pages.home import set_page

# Page Configuration
st.set_page_config(page_title="Job Details", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            background-color: #09090B;
        }
        .job-container {
            text-align: left;
            padding: 20px;
            color: white;
        }
        .company-logo {
            width: 60px;
            height: 60px;
            border-radius: 10px;
            object-fit: cover;
        }
        .job-title {
            font-size: 24px;
            font-weight: bold;
        }
        .location {
            font-size: 16px;
            color: #b3b3b3;
        }
        .tag {
            display: inline-block;
            background-color: black;
            color: white;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 14px;
            margin-right: 5px;
            border: 1px solid #6739B7;
        }
        .apply-save-buttons {
            display: flex;
            gap: 10px;
            margin: 20px 0;
        }
        .apply-btn, .save-btn {
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            text-align: center;
            width: 48%;
        }
        .apply-btn {
            background-color: #6739B7;
            color: white;
        }
        .save-btn {
            background-color: transparent;
            color: white;
            border: 2px solid #6739B7;
        }
        .about-job {
            font-size: 50px;
            font-weight: medium;
            margin: 20px 0;
        }
        .job-description {
            font-size: 14px;
            line-height: 1.6;
            color: #f4f4f4;
            padding: 20px;
            background-color: #333333;
            overflow x-axis: scroll;
            width: 100%;
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

# Job Container
with st.container():
    st.markdown('<div class="job-container">', unsafe_allow_html=True)

    # Company Logo & Name
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://via.placeholder.com/60", width=60)  # Tesla Logo Placeholder
    with col2:
        st.markdown('<p class="job-title">UI/UX Designer</p>', unsafe_allow_html=True)
        st.markdown('<p class="location">Los Angeles, CA</p>', unsafe_allow_html=True)

    # Job Tags
    st.markdown("""
        <span class="tag">Full-time</span>
        <span class="tag">Remote</span>
    """, unsafe_allow_html=True)

    # Apply & Save Buttons
    st.markdown("""
        <div class="apply-save-buttons">
            <span class="apply-btn">Apply now</span>
            <span class="save-btn">Save</span>
        </div>
    """, unsafe_allow_html=True)

    # About Job Section
    st.markdown('<p class="about-job" >About the job</p>', unsafe_allow_html=True)

    # Job Description
    job_description = """
    Micromobility Industries is the world’s largest media brand for small vehicles. 
    We are seeking a creative and versatile Content & Design Specialist to join our team.

    This role is ideal for someone with a passion for content creation, design, and marketing. 
    If you have an eye for detail, an understanding of design aesthetics, and can create compelling 
    content across various formats, we’d love to hear from you!

    **Responsibilities:**
    - Content Creation: Write engaging and informative content for blogs, websites, newsletters, and social media platforms.
    - Presentation Support: Assist in the creation of visually appealing presentations that communicate complex ideas clearly and effectively.
    - Design Marketing Materials: Create eye-catching banners, posters, social media graphics, and other marketing materials.materials to support campaigns.
    -Charts & Data Visualization: Develop aesthetically pleasing and easy-to-understand charts, infographics, and other data visuals.
    -Brand Consistency: Ensure all content and designs align with the company’s brand guidelines and maintain a consistent voice across all touchpoints.
    -Collaboration: Work closely with the marketing, product, and sales teams to understand content and design needs.

    Qualifications:
    -Proven experience in content writing, design, and marketing materials.
    -Strong proficiency in design tools such as Adobe Creative Suite (Illustrator, Photoshop, InDesign), Canva, and PowerPoint.
    -Excellent writing and editing skills with a keen eye for grammar and style.
    -Strong understanding of design principles, color theory, typography, and visual hierarchy.
    -Ability to create compelling presentations and visuals that engage and inform.
    -Ability to work independently and manage multiple projects in a fast-paced environment.
    -A portfolio showcasing design and content work is a plus.

    Additional Skills preferred:
    -Experience with HTML/CSS or other web design tools.
    -Familiarity with video editing or animation tools (e.g., Adobe Premiere, After Effects).

    What We Offer:
    -Opportunity to work in a dynamic, creative environment.
    -Flexible work hours and remote work.
    -A chance to make a significant impact in a growing company.

    How to Apply:
    Please submit your resume along with a portfolio showcasing your design and content work. We look forward to seeing how you can contribute to our team!
    """

    st.markdown(f'<p class="job-description; style="padding:30px">{job_description}</p>', unsafe_allow_html=True)

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

