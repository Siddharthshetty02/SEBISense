# Streamlit frontend starter
import streamlit as st
from pathlib import Path

# Set page config
st.set_page_config(page_title="RegAlert", layout="wide")

# Load CSS
css_file = Path(__file__).parent / "assets" / "style.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("RegAlert Menu")
menu = ["Dashboard", "Alerts", "Chatbot"]
choice = st.sidebar.radio("Go to", menu)

# Import pages dynamically
if choice == "Dashboard":
    from pages import dashboard
elif choice == "Alerts":
    from pages import alerts
elif choice == "Chatbot":
    from pages import chatbot

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 RegAlert | Powered by AI & NLP")
