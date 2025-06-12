import streamlit as st

st.markdown("<h1 style='text-align: center;'>🔐 Login</h1>", unsafe_allow_html=True)

# Email and Password
email = st.text_input("Email", placeholder="Enter your email")
password = st.text_input("Password", type="password", placeholder="Enter your password")

st.markdown(
    """
    <style>
    .stMarkdown {
        text-align: center;
    }
    
    .stButton {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Login button
login = st.button("Login")
if login:
    if email and password:
        st.success("Login successful!")
        st.switch_page("Homepage") 
        # You can add redirect logic here
    else:
        st.error("Please fill in both email and password.")

# Forgot password
st.markdown('<p style="text-align:right"><a href="\ForgotPassword">Forgot password?</a></p>', unsafe_allow_html=True)



st.markdown('<div class="or-divider">(or)</div>', unsafe_allow_html=True)
st.markdown("#####")
# Continue with Google (mock)
google_btn = st.button("Continue with Google")
if google_btn:
    st.info("Google Sign-In is not connected yet (mock button).")

st.markdown("</div>", unsafe_allow_html=True)
