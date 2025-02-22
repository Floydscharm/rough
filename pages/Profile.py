# pages/login.py
import streamlit as st

def main():
    st.markdown(
        """
        <style>
        body {
            background-color: #282828;
            color: white;
        }
        .stTextInput>div>div>input, .stButton>button {
            background-color: #383838;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 8px 12px;
        }
        .stButton>button {
            padding: 10px 15px;
            display: block;
            margin: 10px auto;
        }
        .stTextInput>div>div>input::placeholder {
            color: #888;
        }
        .css-10trblm {
            background-color: #383838;
            border-radius: 5px;
            padding: 8px 12px;
        }
        .css-10trblm:hover {
            background-color: #484848;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1 style='text-align: center;'>Profile</h1>", unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Username")
    phone = st.text_input("Phone number", placeholder="Phone number")

    if st.button("My resume"):
        # Placeholder for resume logic
        st.write("Displaying resume...") #Replace with actual logic

    if st.button("Edit"):
        # Placeholder for edit logic
        st.write("Editing profile...") #Replace with actual logic

if __name__ == "__main__":
    main()