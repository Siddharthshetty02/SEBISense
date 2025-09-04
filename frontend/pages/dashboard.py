# dashboard page placeholder
import streamlit as st
import requests

st.title("📝 Regulatory Summarizer")

# Backend API endpoint
SUMMARIZE_API = "http://localhost:5000/summarize"

# Input box for SEBI circular / text
text_input = st.text_area("Paste SEBI Circular or Regulatory Update Here:")

if st.button("Generate Summary"):
    if not text_input.strip():
        st.warning("Please provide text to summarize.")
    else:
        try:
            response = requests.post(SUMMARIZE_API, json={"text": text_input})
            if response.status_code == 200:
                data = response.json()
                summary = data.get('summary', '')
                alerts = data.get('alerts', [])
                
                # Display summary
                st.markdown(
                    f"<div class='summary-box'><strong>Summary:</strong><br>{summary}</div>",
                    unsafe_allow_html=True
                )
                
                # Display generated alerts
                if alerts:
                    st.subheader("Generated Alerts")
                    for alert in alerts:
                        st.markdown(
                            f"<div class='alert'>{alert}</div>",
                            unsafe_allow_html=True
                        )
                else:
                    st.info("No alerts generated for this circular.")
            else:
                st.error(f"Error from backend: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
