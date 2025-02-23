
# Custom CSS for exact styling
import streamlit as st
st.markdown(
    """
    <style>
        body {
            background-color: #09090b;
        }
        .container {
            max-width: 400px;
            margin: auto;
            padding-top: 30px;
        }
        .title {
            text-align: center;
            font-family: 'Inter', sans-serif;
            font-size: 28px;
            font-weight: 700;
            color: white;
            margin-bottom: 40px;
        }
        .input-box label {
            font-family: 'Inter', sans-serif;
            font-size: 18px;
            font-weight: 600;
            color: #1a2421;
        }
        .input-box input {
            width: 100%;
            padding: 12px;
            border-radius: 15px;
            border: none;
            font-size: 18px;
            background-color: #f8f1ec;
            color: #1a2421;
            margin-bottom: 20px;
        }
        .register-btn {
            background-color: #d5621d;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 12px;
            border: none;
            border-radius: 15px;
            width: 100%;
            text-align: center;
            cursor: pointer;
            margin-top: 20px;
        }
        .login-link {
            text-align: center;
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            color: white;
            margin-top: 20px;
        }
        .login-link a {
            color: #d5621d;
            font-weight: bold;
            text-decoration: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page content
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>REGISTER</div>", unsafe_allow_html=True)

# Input fields
name = st.text_input("Name", key="name", placeholder="Name", label_visibility="collapsed")
phone = st.text_input("Phone number", key="phone", placeholder="Phone number", label_visibility="collapsed")
email = st.text_input("E-mail", key="email", placeholder="E-mail", label_visibility="collapsed")
password = st.text_input("Password", key="password", placeholder="Password", type="password", label_visibility="collapsed")

# Register button
if st.button("REGISTER", key="register"):
    st.success(f"Welcome, {name}! You have successfully registered.")

# Login link
st.markdown(
    "<div class='login-link'>Already have an account? <a href='#'>Login</a></div>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)


