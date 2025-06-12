import streamlit as st
from PIL import Image
import os
import base64
from io import BytesIO

# Set page config
st.set_page_config(page_title="ReadCycle", page_icon="📚", layout="centered")

# Dark mode styling
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #FFFFFF;
    }
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f1f1f;
        color: white;
        border: 1px solid #ffffff55;
        padding: 10px;
        font-size: 16px;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #333333;
        color: #ffd700;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to convert logo image to base64
def logo_to_base64(image):
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str

# Center logo
logo_path = os.path.join("assets", "logo.jpg")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.markdown(
        f"<div style='text-align: center;'><img src='data:image/jpg;base64,{logo_to_base64(logo)}' width='230'/></div>",
        unsafe_allow_html=True
    )
else:
    st.warning("Logo image not found. Please place logo.jpg inside the 'assets/' folder.")

# Title and tagline
st.markdown("<h1 style='text-align: center; color: white;'>ReadCycle</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>📚 Read. Return. Repeat 📚</h4>", unsafe_allow_html=True)

# Centered CTA Buttons
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("Login"):
            st.switch_page("pages/0_Login.py")
    with col_btn2:
        if st.button("Register"):
            st.switch_page("pages/1_Register.py")

st.markdown("---")
st.markdown("<div style='text-align:center; background-color: #5284bd; color: #ffffff; border-radius: 10px; padding: 8px; margin-bottom: 10px;'>Use buttons above to get started.</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div style='text-align:center; font-size: 12px; color: gray;'>Made with ❤ by Team ReadCycle</div>", unsafe_allow_html=True)
