import streamlit as st

# Set Page Config
st.set_page_config(page_title="Login", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            background-color: #09090B;
            text-align: center;
        }
        .stTextInput, .stButton>button {
            border-radius: 10px;
        }
        .login-container {
            text-align: center;
            margin-top: 50px;
        }
        .login-title {
            font-size: 30px;
            font-weight: medium;
            color: white;
        }
        .login-btn {
            background-color: #6739B7 !important;
            color: white !important;
            width: 100%;
            border-radius: 10px;
        }
        .or-divider {
            margin: 10px 0;
            color: gray;
            font-size: 15px;
        }
        .register-text {
            color: white;
            font-size: 14px;
        }
        .register-link {
            color: #6739B7;
            text-decoration: none;
            font-weight: bold;
            cursor: pointer;
        }
        .oauth-btn {
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid white;
            border-radius: 10px;
            padding: 10px;
            color: white;
            margin-top: 10px;
            background-color: transparent;
        }
        .oauth-icon {
            margin-left: auto;
        }
    .textInput {
        width: 100%;
        padding: 12px;
        border-radius: 15px;
        border: none;
        font-size: 18px;
        background-color: #f8f1ec;
        color: #1a2421;
        margin-bottom: 20px;
    }
    
    
    </style>
""", unsafe_allow_html=True)
    
# Session state to handle transition
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
st.title("Login")
def login():
    st.session_state.logged_in = True
    st.experimental_rerun()  # Rerun the app to navigate to the home page

            
def button2():
    with col2:
            st.button("Login with Google", key="google_btn", help="Login with Google", args=("google",))
            st.button("Login with Github", key="github_btn", help="Login with Github", args=("github",))
if not st.session_state.logged_in:
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        

        username = st.text_input("User name", key="username")
        password = st.text_input("Password", type="password", key="password")
        if st.button("Login", key="login_btn", help="Click to login"):
                if username and password:
                    login()
        
        st.markdown('<p class="or-divider">──────── OR ────────</p>', unsafe_allow_html=True)
        st.markdown('<p class="register-text">Don’t have an account? <span class="register-link">Register</span></p>', unsafe_allow_html=True)
        col1,col2,col3 = st.columns([1,0.6,1],vertical_alignment="bottom",gap="small")
        button2()
        
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.success(f"Welcome, {st.session_state.username}!")
    st.write("This is your home page now.")  # You can redirect to home/dashboard here
