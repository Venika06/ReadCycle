# File: pages/Profile.py

import streamlit as st

st.set_page_config(page_title="📄 Profile", layout="centered")

st.markdown("<h1 style='text-align: center;'>👤 User Profile</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Please fill out your profile details below:</h6>", unsafe_allow_html=True)

st.markdown("######")
# Basic Info
st.markdown("<h4 style='text-align: left;'>📋 Basic Information</h4>", unsafe_allow_html=True)
#st.subheader("📋 Basic Information")
name = st.text_input("Full Name")
phone = st.text_input("Phone Number (Indian)", max_chars=10)

# Address Section
st.markdown("<h4 style='text-align: left;'>🏠 Address Information</h4>", unsafe_allow_html=True)
#st.subheader("🏠 Address Information")
door_no = st.text_input("Door No.")
area = st.text_input("Area / Street")
landmark = st.text_input("Landmark")
city = st.text_input("City / Village")
mandal = st.text_input("Mandal")
district = st.text_input("District")
state = st.text_input("State")

# Additional Details
st.markdown("<h4 style='text-align: left;'>📝 Additional Info</h4>", unsafe_allow_html=True)
#st.subheader("📝 Additional Info")
bio = st.text_area("Bio (optional)", help="A short description about yourself", height=100)
fav_book = st.text_input("Favorite Book")
fav_author = st.text_input("Favorite Author")
fav_genre = st.text_input("Favorite Genre")
others = st.text_area("Other Notes / Preferences")

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

# Submit Button
if st.button("💾 Save Profile"):
    if name and phone and door_no and city and district and state:
        st.success("✅ Profile saved successfully!")
        st.markdown("#### 📋 Summary")
        st.write(f"**Name:** {name}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Address:** {door_no}, {area}, {landmark}, {city}, {mandal}, {district}, {state}")
        if bio:
            st.write(f"**Bio:** {bio}")
        st.write(f"**Favorite Book:** {fav_book}")
        st.write(f"**Favorite Author:** {fav_author}")
        st.write(f"**Genre:** {fav_genre}")
        st.write(f"**Other:** {others}")
    else:
        st.error("⚠️ Please fill in all the required fields: name, phone, door no, city, district, and state.")
