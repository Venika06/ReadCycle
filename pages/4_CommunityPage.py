from pages.nav import bottom_nav
import streamlit as st

from pages.nav import bottom_nav
import streamlit as st

st.title()
# your content here...


# --- PAGE CONFIG ---
st.set_page_config(page_title="Community", page_icon="👥", layout="wide")

# --- HEADER ---
st.markdown(
    """
    <h1 style='text-align: center; color: #08A508;'>👥 Community</h1>
    """,
    unsafe_allow_html=True
)

# --- COMMUNITY SECTIONS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔥 Book Clubs")
    st.write("Join clubs that match your reading tastes.")
    if st.button("Explore Book Clubs"):
        st.success("👉 Navigate to Book Clubs page (to implement)")

with col2:
    st.markdown("### 📍 Nearby Readers")
    st.write("Find readers around you.")
    if st.button("Find Nearby Readers"):
        st.success("👉 Navigate to Nearby Readers page (to implement)")

with col3:
    st.markdown("### 🤝 Similar Readers")
    st.write("Connect with users who like what you read.")
    if st.button("Find Similar Readers"):
        st.success("👉 Navigate to Similar Readers page (to implement)")

# --- SIMULATED FLOATING AI CHAT BUTTON ---
# Using a sidebar button to simulate chat button
with st.sidebar:
    st.markdown("---")
    st.markdown("### 💬 Ask AI")
    ai_query = st.text_input("Type your question:")
    if st.button("Ask AI"):
        if ai_query:
            # Here, you'd connect to your AI backend (OpenAI, HuggingFace etc)
            st.success(f"AI says: Recommended books for '{ai_query}' (demo response)")
        else:
            st.warning("Please type a question for AI recommendations.")


bottom_nav(active="community")


bottom_nav(active="community")
