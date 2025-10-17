import streamlit as st
import requests

# Define the base URL for the FastAPI backend
BACKEND_URL = "http://127.0.0.1:8000"

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Unthinkable RAG Engine",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Knowledge-base Search Engine")

# --- Document Upload Section ---
st.header("1. Upload a Document")
uploaded_file = st.file_uploader(
    "Choose a PDF file to add to the knowledge base.", 
    type="pdf"
)

if uploaded_file is not None:
    # When a file is uploaded, send it to the backend's /ingest endpoint
    files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
    with st.spinner('Ingesting document... This may take a moment.'):
        try:
            response = requests.post(f"{BACKEND_URL}/ingest", files=files)
            if response.status_code == 200:
                st.success(f"Successfully ingested '{uploaded_file.name}'!")
            else:
                st.error(f"Error ingesting file: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to the backend: {e}")

st.divider()

# --- Query Section ---
st.header("2. Ask a Question")
question = st.text_input("Enter your question about the uploaded document(s).")

if st.button("Get Answer"):
    if question:
        # When the button is clicked, send the question to the backend's /query endpoint
        payload = {"question": question}
        with st.spinner('Searching for an answer...'):
            try:
                response = requests.post(f"{BACKEND_URL}/query", json=payload)
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer found.")
                    st.success("Answer:")
                    st.write(answer)
                else:
                    st.error(f"Error getting answer: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Could not connect to the backend: {e}")
    else:
        st.warning("Please enter a question.")