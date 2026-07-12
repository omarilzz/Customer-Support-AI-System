import streamlit as st
import requests

st.title("Customer Support AI System")
ticket_text = st.text_area("Enter Ticket Description")

if st.button("Predict"):
    st.write("Sending request to API...") # Feedback
    try:
        # Use a short timeout so it doesn't hang forever
        response = requests.post("http://127.0.0.1:8000/predict", json={"text": ticket_text}, timeout=10)
        
        if response.status_code == 200:
            st.success(f"Result: {response.json()['prediction']}")
        else:
            st.error(f"API returned status {response.status_code}")
            st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
