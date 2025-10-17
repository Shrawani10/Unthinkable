# Unthinkable: Knowledge-base Search Engine

This project is a knowledge-base search engine that allows users to search across multiple documents and receive synthesized answers.  
It uses a Retrieval-Augmented Generation (RAG) pipeline powered by a local Large Language Model (LLM) to provide accurate, context-aware responses based on uploaded content.

---------------------------------
## 1. Features
---------------------------------

1. PDF Document Ingestion  
   Upload PDF documents via a REST API endpoint.

2. Dynamic Knowledge Base  
   Documents are automatically chunked, embedded using a sentence-transformer model, and stored in a persistent ChromaDB vector store.

3. AI-Powered Q&A  
   A query endpoint leverages a RAG chain to retrieve relevant context from stored documents and generate concise, natural language answers.

4. Local First  
   The entire pipeline runs locally using Ollama to serve a powerful LLM (phi3) without relying on external APIs.

5. Decoupled Architecture  
   The system is built with a separate FastAPI backend for logic and an optional React frontend for user interaction.

---------------------------------
## 2. Tech Stack
---------------------------------

- Backend: Python, FastAPI  
- RAG Orchestration: LangChain  
- LLM Service: Ollama  
- LLM: Microsoft Phi-3  
- Vector Store: ChromaDB  
- Embedding Model: Sentence-Transformers (all-MiniLM-L-6-v2)  
- Frontend: React (with Vite)

---------------------------------
## 3. Setup and Installation
---------------------------------

Follow these steps to set up and run the project locally.

### 3.1 Prerequisites

- Python 3.8+  
- Git  
- Ollama  
- Node.js and npm (for the frontend)

### 3.2 Clone the Repository

Clone this repository to your local machine.

git clone https://github.com/Shrawani10/Unthinkable.git  
cd Unthinkable

### 3.3 Set Up the Backend

All commands should be run from the root Unthinkable directory.

#### a. Create and Activate Virtual Environment

# Create the environment  
python -m venv venv  

# Activate the environment (Windows)  
venv\Scripts\activate  

# Activate the environment (macOS/Linux)  
source venv/bin/activate  

#### b. Install Python Dependencies

pip install -r requirements.txt  

#### c. Download the Required Models

# Ollama LLM: Pull the Phi-3 model  
ollama pull phi3  

# Embedding Model: Clone the sentence-transformer model into a local folder named local_model  
git clone https://huggingface.co/sentence-transformers/all-MiniLM-L-6-v2 local_model  

---------------------------------
## 4. Running the Application
---------------------------------

The application requires two separate terminals to run both the backend and the frontend.

### 4.1 Terminal 1 – Start the Backend Server

Make sure the Ollama application is running in the background.

# Make sure you are in the 'Unthinkable' folder and the venv is active  
python -m uvicorn main:app --reload  

The API will be available at:  
http://127.0.0.1:8000

### 4.2 Terminal 2 – Start the Frontend (Optional)

If you have set up the unthinkable-ui project, run it in a second terminal.

# Navigate to your UI project folder  
cd ../unthinkable-ui  

# Start the React development server  
npm run dev  

The UI will be available at:  
http://localhost:5173  
(or a similar address shown in the terminal)

---------------------------------
## 5. API Usage
---------------------------------

You can interact with the API directly via the automatic documentation at:  
http://127.0.0.1:8000/docs  
or by using a tool like curl.

### 5.1 Ingest a Document

Upload a PDF file to be processed and stored in the vector database.

Endpoint: POST /ingest  

Example command:  
curl -X POST -F "file=@/path/to/your/document.pdf" http://127.0.0.1:8000/ingest  

### 5.2 Ask a Question

Ask a question and receive a synthesized answer based on the ingested documents.

Endpoint: POST /query  

Request Body:  
{
  "question": "Your question here"
}

Example command:  
curl -X POST -H "Content-Type: application/json" -d "{\"question\": \"What is light?\"}" http://127.0.0.1:8000/query  
