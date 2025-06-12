# File: Homepage.py
import streamlit as st
from pages.nav import bottom_nav

st.set_page_config(page_title="Homepage", layout="wide")

# --- Header with HTML/CSS/JS ---
st.markdown("""
<style>
.header-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: nowrap;
    gap: 10px;
    margin-bottom: 10px;
}
.search-container {
    flex-grow: 1;
    position: relative;
}
#voice-search {
    width: 100%;
    padding: 10px 40px 10px 10px;
    font-size: 16px;
    border-radius: 8px;
    border: 1px solid #ccc;
}
.mic-icon {
    position: absolute;
    right: 40px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
    cursor: pointer;
}
.notify-icon {
    font-size: 22px;
    cursor: pointer;
    padding: 8px;
    border-radius: 50%;
    text-align: center;
    background-color: #000000;
}
.notify-icon:hover {
    background-color: #000000;
}
@media screen and (max-width: 768px) {
    .header-bar {
        flex-direction: row;
    }
}
</style>

<div class="header-bar">
    <div class="search-container">
        <input id="voice-search" placeholder="Search books, authors, genres..." />
        <span class="mic-icon" onclick="startListening()">🎙️</span>
    </div>
    <a href="/NotificationPage" target="_self" class="notify-icon" title="Notifications" style="text-decoration: none;">🔔</a>
</div>

<script>
    const inputBox = document.getElementById("voice-search");
    function startListening() {
        try {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            const recognition = new SpeechRecognition();
            recognition.lang = 'en-US';
            recognition.interimResults = false;
            recognition.maxAlternatives = 1;

            recognition.start();

            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                inputBox.value = transcript;
                inputBox.dispatchEvent(new Event('input', { bubbles: true }));
            };

            recognition.onerror = function(event) {
                alert("Voice recognition error: " + event.error);
            };
        } catch (e) {
            alert("Your browser does not support Speech Recognition.");
        }
    }
</script>
""", unsafe_allow_html=True)


st.markdown("---")

# --- Genre Carousel ---
st.markdown("### 🎭 Browse by Genre")
genres = ["Fiction", "Non-fiction", "Sci-Fi", "Self-help", "Academic", "Mystery", "Romance", "Fantasy"]
genre_cols = st.columns(len(genres))
for i, genre in enumerate(genres):
    with genre_cols[i]:
        if st.button(f"📘 {genre}"):
            st.session_state.selected_genre = genre

# --- AI Recommendations ---
st.markdown("### 🤖 AI Picks for You")
ai_books = [
    {"title": "The Alchemist", "emoji": "🧙‍♂️"},
    {"title": "Atomic Habits", "emoji": "💥"},
    {"title": "Sapiens", "emoji": "🧠"},
]
ai_cols = st.columns(len(ai_books))
for i, book in enumerate(ai_books):
    with ai_cols[i]:
        st.markdown(f"{book['emoji']} **{book['title']}**")
        st.button("🔍 View", key=f"view_{i}")
        st.button("💖 Save", key=f"save_{i}")

# --- Book Grid Section ---
st.markdown("### 📚 Books Near You")
selected_filters = st.multiselect("Apply Filters", ["Fiction", "New Arrival", "Near You", "Give", "Swap"])

books = [
    {"title": "1984", "tag": "Trending"},
    {"title": "Ikigai", "tag": "Near You"},
    {"title": "Rich Dad Poor Dad", "tag": "New Arrival"},
]
grid_cols = st.columns(3)
for i, book in enumerate(books):
    with grid_cols[i % 3]:
        st.markdown(f"📖 **{book['title']}**")
        st.markdown(f"🟢 *{book['tag']}*")
        st.button("📬 Request", key=f"req_{i}")

# --- Floating Filter Button (Basic Emulation) ---
st.markdown("""
    <style>
        #filter-button {
            position: fixed;
            bottom: 90px;
            right: 20px;
            z-index: 100;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            font-size: 24px;
        }
    </style>
    <button id="filter-button">⚙️</button>
""", unsafe_allow_html=True)

# --- Bottom Navigation Bar ---
bottom_nav(active="homepage")

