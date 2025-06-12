# File: pages/_ForgotPassword.py

import streamlit as st

st.markdown("<h2 style='text-align: center;'>🤔 Forgot Password</h2>", unsafe_allow_html=True)

st.markdown("#####")
# Email input
email = st.text_input("Email", placeholder="Enter your registered email")

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

# Centered "Send OTP" button
col1, col2, col3 = st.columns([2, 2, 1])
with col2:
    if st.button("Send OTP"):
        if email:
            st.session_state.email = email  # Store for OTP page
            st.success("OTP sent to your email.")
            st.switch_page("pages/_VerifyOTP.py")
        else:
            st.error("Please enter a valid email.")
