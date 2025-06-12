import streamlit as st
import re

st.set_page_config(page_title="Register - ReadCycle", layout="centered")

# Centered Title
st.markdown("<h1 style='text-align: center;'>📝 Register</h1>", unsafe_allow_html=True)

# Input Fields
full_name = st.text_input("Full Name", placeholder="Enter your full name")
email = st.text_input("Email", placeholder="Enter your email address")
phone = st.text_input("Phone Number", placeholder="Enter your 10-digit mobile number")
password = st.text_input("Password", type="password", placeholder="Create a password")
confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password")

# Validation function
def is_valid_phone(phone):
    return re.fullmatch(r"[6-9]\d{9}", phone)

st.markdown(
    """
    <style>
    .stButton {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Register Button (Centered)
col1, col2, col3 = st.columns([2.5, 2, 1.5])
with col2:
    if st.button("Register"):
        if not full_name or not email or not phone or not password or not confirm_password:
            st.error("⚠️ Please fill out all fields.")
        elif not is_valid_phone(phone):
            st.error("📱 Enter a valid 10-digit Indian mobile number.")
        elif password != confirm_password:
            st.error("🔒 Passwords do not match.")
        else:
            st.success(f"🎉 Registered successfully as {full_name}!")
            # Here you can add code to save user details