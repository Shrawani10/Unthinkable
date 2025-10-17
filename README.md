Unthinkable: Knowledge-base Search Engine

This project is a knowledge-base search engine that allows users to search across multiple documents and receive synthesized answers. It uses a Retrieval-Augmented Generation (RAG) pipeline powered by a local Large Language Model (LLM) to provide accurate, context-aware responses based on uploaded content.

Features:
- PDF Document Ingestion: Upload PDF documents via a REST API endpoint.
- Dynamic Knowledge Base: Documents are automatically chunked, embedded using a sentence-transformer model, and stored in a persistent ChromaDB vector store.
- AI-Powered Q&A: A query endpoint leverages a RAG chain to retrieve relevant context from stored documents and generate concise, natural language answers.
- Local First: The entire pipeline runs locally using Ollama to serve a powerful LLM (phi3) without relying on external APIs.
- Decoupled Architecture: The system is built with a separate FastAPI backend for logic and an optional React frontend for user interaction.

Tech Stack:
- Backend: Python, FastAPI
- RAG Orchestration: LangChain
- LLM Service: Ollama
- LLM: Microsoft Phi-3
- Vector Store: ChromaDB
- Embedding Model: Sentence-Transformers (all-MiniLM-L-6-v2)
- Frontend: React (with Vite)

Setup and Installation:
Follow these steps to set up and run the project locally.

Prerequisites:
- Python 3.8+
- Git
- Ollama
- Node.js and npm (for the frontend)

1. Clone the Repository
---------------------------------
git clone https://github.com/Shrawani10/Unthinkable.git
cd Unthinkable

2. Set Up the Backend
---------------------------------
All these commands should be run from the root Unthinkable directory.

a. Create and Activate Virtual Environment:
---------------------------------
# Create the environment
python -m venv venv

# Activate the environment (Windows)
venv\Scripts\activate

# Activate the environment (macOS/Linux)
source venv/bin/activate

b. Install Python Dependencies:
---------------------------------
pip install -r requirements.txt

c. Download the Required Models:
---------------------------------
# Ollama LLM: Pull the phi3 model
ollama pull phi3

# Embedding Model: Clone the sentence-transformer model
git clone https://huggingface.co/sentence-transformers/all-MiniLM-L-6-v2 local_model

3. How to Run
---------------------------------
The application requires two separate terminals to run both the backend and the frontend.

Terminal 1: Start the Backend Server
---------------------------------
# Make sure Ollama is running in the background
python -m uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000

Terminal 2: Start the Frontend (Optional)
---------------------------------
# Navigate to your UI project folder
cd ../unthinkable-ui

# Start the React development server
npm run dev

The UI will be available at http://localhost:5173

API Usage:
---------------------------------
You can interact with the API via http://127.0.0.1:8000/docs or use curl.

Ingest a Document:
---------------------------------
Endpoint: POST /ingest

curl -X POST -F "file=@/path/to/your/document.pdf" http://127.0.0.1:8000/ingest

Ask a Question:
---------------------------------
Endpoint: POST /query

Request Body:
{
  "question": "Your question here"
}

Example:
curl -X POST -H "Content-Type: application/json" -d "{\"question\": \"What is light?\"}" http://127.0.0.1:8000/query

