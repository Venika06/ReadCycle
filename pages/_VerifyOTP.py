# File: pages/_VerifyOTP.py

import streamlit as st

st.set_page_config(page_title="Verify OTP", layout="centered")

# Custom styling
st.markdown("""
    <style>
    .otp-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        margin-top: 20px;
    }
    .otp-box input {
        width: 60px !important;
        height: 60px !important;
        text-align: center;
        font-size: 24px;
        border: 2px solid #ccc;
        border-radius: 8px;
    }
    .stButton button {
        width: 100%;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🔑 Verify OTP</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter the 4-digit OTP sent to your email</p>", unsafe_allow_html=True)

# OTP input fields in one row
st.markdown('<div class="otp-container">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="otp-box">', unsafe_allow_html=True)
    d1 = st.text_input(" ", max_chars=1, key="otp1", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="otp-box">', unsafe_allow_html=True)
    d2 = st.text_input(" ", max_chars=1, key="otp2", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="otp-box">', unsafe_allow_html=True)
    d3 = st.text_input(" ", max_chars=1, key="otp3", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="otp-box">', unsafe_allow_html=True)
    d4 = st.text_input(" ", max_chars=1, key="otp4", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Concatenate OTP
otp_entered = d1 + d2 + d3 + d4

# Verify Button
st.markdown("###")
col_btn = st.columns(3)[1]
with col_btn:
    if st.button("✅ Verify OTP"):
        if len(otp_entered) == 4 and otp_entered.isdigit():
            st.success("✅ OTP Verified!")
        else:
            st.error("❌ Please enter a valid 4-digit OTP.")

# Resend OTP Button
st.markdown("###")
colx1, colx2 = st.columns([7, 3])
with colx2:
    if st.button("🔁 Resend OTP"):
        st.markdown(
            "<p style='text-align:center; color:green;'>A new OTP has been sent to your email.</p>",
            unsafe_allow_html=True
        )
