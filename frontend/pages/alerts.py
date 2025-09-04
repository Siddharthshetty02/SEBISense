# alerts page placeholder
import streamlit as st
import requests

st.set_page_config(page_title="RegAlert Alerts")
st.title("📢 Regulatory Alerts")

# Backend API endpoint
ALERTS_API = "http://localhost:5000/alerts"

def fetch_alerts():
    try:
        response = requests.get(ALERTS_API)
        if response.status_code == 200:
            return response.json().get('alerts', [])
        else:
            st.error(f"Error fetching alerts: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
        return []

# Display alerts
alerts = fetch_alerts()
if alerts:
    for alert in alerts:
        st.markdown(
            f"""
            <div class="alert">
                <strong>Circular:</strong> {alert['circular_title']}<br>
                <strong>Message:</strong> {alert['message']}<br>
                <small>{alert['date_created']}</small>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("No alerts available at the moment.")
