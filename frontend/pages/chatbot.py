# chatbot page placeholder
import streamlit as st
import requests

st.title("💬 Regulatory Q&A Chatbot")

# Backend API endpoint
CHATBOT_API = "http://localhost:5000/ask"

# Input for context (optional) and question
context_input = st.text_area("Provide context (optional, e.g., circular text):")
question_input = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if not question_input.strip():
        st.warning("Please enter a question.")
    else:
        try:
            response = requests.post(CHATBOT_API, json={
                "question": question_input,
                "context": context_input
            })
            if response.status_code == 200:
                data = response.json()
                answer = data.get('answer', 'No answer returned.')
                # Display chatbot answer
                st.markdown(
                    f"<div class='chat-box'><strong>Answer:</strong><br>{answer}</div>",
                    unsafe_allow_html=True
                )
            else:
                st.error(f"Error from backend: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
