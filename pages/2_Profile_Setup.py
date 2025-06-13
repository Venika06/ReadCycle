import streamlit as st

st.set_page_config(page_title="📄 Profile", layout="centered")

st.markdown("<h1 style='text-align: center;'>👤 User Profile</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Please fill out your profile details below:</h6>", unsafe_allow_html=True)

# --- INPUTS ---
name = st.text_input("Full Name", value=st.session_state.get("profile_name", ""))
phone = st.text_input("Phone Number (Indian)", max_chars=10, value=st.session_state.get("profile_phone", ""))

door_no = st.text_input("Door No.", value=st.session_state.get("profile_door_no", ""))
area = st.text_input("Area / Street", value=st.session_state.get("profile_area", ""))
landmark = st.text_input("Landmark", value=st.session_state.get("profile_landmark", ""))
city = st.text_input("City / Village", value=st.session_state.get("profile_city", ""))
mandal = st.text_input("Mandal", value=st.session_state.get("profile_mandal", ""))
district = st.text_input("District", value=st.session_state.get("profile_district", ""))
state = st.text_input("State", value=st.session_state.get("profile_state", ""))

bio = st.text_area("Bio (optional)", help="A short description about yourself", height=100, value=st.session_state.get("profile_bio", ""))
fav_book = st.text_input("Favorite Book", value=st.session_state.get("profile_fav_book", ""))
fav_author = st.text_input("Favorite Author", value=st.session_state.get("profile_fav_author", ""))
fav_genre = st.text_input("Favorite Genre", value=st.session_state.get("profile_fav_genre", ""))
others = st.text_area("Other Notes / Preferences", value=st.session_state.get("profile_others", ""))

if st.button("💾 Save Profile"):
    if name and phone and door_no and city and district and state:
        st.session_state["profile_name"] = name
        st.session_state["profile_phone"] = phone
        st.session_state["profile_door_no"] = door_no
        st.session_state["profile_area"] = area
        st.session_state["profile_landmark"] = landmark
        st.session_state["profile_city"] = city
        st.session_state["profile_mandal"] = mandal
        st.session_state["profile_district"] = district
        st.session_state["profile_state"] = state
        st.session_state["profile_bio"] = bio
        st.session_state["profile_fav_book"] = fav_book
        st.session_state["profile_fav_author"] = fav_author
        st.session_state["profile_fav_genre"] = fav_genre
        st.session_state["profile_others"] = others
        st.success("✅ Profile saved successfully!")
    else:
        st.error("⚠️ Please fill in all required fields: name, phone, door no, city, district, and state.")
