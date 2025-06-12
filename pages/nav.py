# File: components/nav.py
import streamlit as st

def bottom_nav(active="homepage"):
    st.markdown(f"""
    <style>
    .bottom-nav {{
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 60px;
        background-color: #000000;
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 9999;
    }}
    .nav-item {{
        font-size: 14px;
        text-align: center;
        color: #ffffff;
    }}
    .nav-item a {{
        text-decoration: none;
        color: inherit;
    }}
    .nav-item.active {{
        color: #007BFF;  /* Blue highlight for active tab */
        font-weight: bold;
    }}
    </style>

    <div class="bottom-nav">
        <div class="nav-item {'active' if active == 'homepage' else ''}">
            <a href="/Homepage" target="_self">🏠<br>Home</a>
        </div>
        <div class="nav-item {'active' if active == 'community' else ''}">
            <a href="/CommunityPage" target="_self">👥<br>Community</a>
        </div>
        <div class="nav-item {'active' if active == 'wishlist' else ''}">
            <a href="/Wishlist" target="_self">❤️<br>Wishlist</a>
        </div>
        <div class="nav-item {'active' if active == 'profile' else ''}">
            <a href="/MyProfile" target="_self">👤<br>Profile</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
