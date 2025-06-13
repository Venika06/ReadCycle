from pages.nav import bottom_nav
import streamlit as st

from pages.nav import bottom_nav
import streamlit as st


st.set_page_config(page_title="👤 My Profile", layout="centered")

st.markdown("<h1 style='text-align: center;'>👑 My Profile</h1>", unsafe_allow_html=True)

# --- DISPLAY PROFILE ---
if "profile_name" in st.session_state:
    st.markdown(f"### {st.session_state['profile_name']}")
    st.write(f"**Phone:** {st.session_state['profile_phone']}")
    st.write(f"**Address:** {st.session_state['profile_door_no']}, {st.session_state['profile_area']}, {st.session_state['profile_landmark']}, {st.session_state['profile_city']}, {st.session_state['profile_mandal']}, {st.session_state['profile_district']}, {st.session_state['profile_state']}")
    if st.session_state['profile_bio']:
        st.write(f"**Bio:** {st.session_state['profile_bio']}")
    st.write(f"**Favorite Book:** {st.session_state['profile_fav_book']}")
    st.write(f"**Favorite Author:** {st.session_state['profile_fav_author']}")
    st.write(f"**Genre:** {st.session_state['profile_fav_genre']}")
    st.write(f"**Other:** {st.session_state['profile_others']}")
else:
    st.warning("⚠️ No profile data found. Please fill your profile in the Profile Setup page.")

# --- EDIT BUTTON ---
if st.button("✏️ Edit Profile"):
    st.info("👉 Please go to the **Profile** page to edit your details.")

# --- HISTORY & ACHIEVEMENTS ---
st.markdown("---")
st.markdown("### 📚 Exchange / Borrow / Donate History")
# Mockup history — replace with real data source
history = st.session_state.get("history", [
    {"type": "Exchange", "book": "The Alchemist", "date": "2024-05-01"},
    {"type": "Donate", "book": "Harry Potter", "date": "2024-05-15"},
])
for record in history:
    st.write(f"✅ {record['type']} - *{record['book']}* on {record['date']}")

st.markdown("### 🏆 Achievements & Badges")
num_exchanges = len([h for h in history if h['type'] == "Exchange"])
num_donates = len([h for h in history if h['type'] == "Donate"])

st.write(f"**Books Exchanged:** {num_exchanges}")
st.write(f"**Books Donated:** {num_donates}")

# Badges
if num_exchanges >= 5:
    st.success("🏅 Exchange Pro")
if num_donates >= 3:
    st.success("🎖️ Generous Donor")

# Streak (mock)
st.markdown("### 🔥 Streaks")
st.write("📈 3-week active participation streak!")

# Personalized stats
st.markdown("### 📊 Personalized Stats")
st.write(f"📘 Favorite Genre: {st.session_state.get('profile_fav_genre', 'N/A')}")
st.write("⭐ Avg books exchanged per month: 2 (demo data)")


bottom_nav(active="profile")


bottom_nav(active="profile")
