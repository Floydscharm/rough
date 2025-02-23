import streamlit as st

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
        .profile-header {
            background-color: #2A2A2A;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .profile-pic {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin-bottom: 10px;
        }
        .message-button {
            background-color: #8A2BE2;
            color: white;
            padding: 10px;
            width: 100%;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
        }
        .section {
            background-color: #1E1E1E;
            padding: 15px;
            margin-top: 10px;
            border-radius: 10px;
        }
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 5px;
        }
        .tech-box {
            background-color: #333;
            padding: 5px 10px;
            border-radius: 10px;
            font-size: 12px;
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
     .nav-icon {
         color: white;
         text-align: center;
         flex: 1;
        }
        .profile-icon {
     position: absolute;
     top: -5500%;
     right: 15px;
     width: 40px;
     height: 40px;
     border-radius: 50%;
     object-fit: cover;
     border: 2px solid white;
    }
    .top-navbar{
        position: absolute;
        top: -750px;
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
     .hamburger {
         position: absolute;
         margin-top: 10px;
         left: 15px;
         font-size: 40Spx;
         color: white;
         cursor: pointer;
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
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Profile section
st.markdown(
    """
    <div class='profile-header'>
        <img class='profile-pic' src='SelectedEemployee.png'/>
        <h2>Sneha Chakraborty (She/Her)</h2>
        <p>Student at Academy of Technology</p>
        <p>Academy of Technology<br>Kolkata, West Bengal</p>
        <div class='message-button'>Message</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Activity section
st.markdown(
    """
    <div class='section'>
        <h3>Activity</h3>
        <p>41 followers</p>
        <img src='Jobs.png' width='100%'/>
        <div style='text-align: center; margin-top: 10px;'>
            <button style='padding: 8px 15px; background-color: #333; color: white; border-radius: 10px;'>Find more</button>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Tech stack section
st.markdown("""
    <div class='section'>
        <h3>Tech stacks</h3>
        <div class='tech-stack'>
            <span class='tech-box'>Python</span>
            <span class='tech-box'>Django</span>
            <span class='tech-box'>React</span>
            <span class='tech-box'>JavaScript</span>
            <span class='tech-box'>Node.js</span>
            <span class='tech-box'>Vue.js</span>
        </div>
    </div>
""", unsafe_allow_html=True)
# Fixed Top Navbar
st.markdown(
    """
    <div class="top-navbar">
        <span class="menu-icon">☰</span>
       
        
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