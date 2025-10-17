# Unthinkable: Knowledge-base Search Engine

This project is a knowledge-base search engine that allows users to search across multiple documents and receive synthesized answers. It uses a Retrieval-Augmented Generation (RAG) pipeline powered by a local Large Language Model (LLM) to provide accurate, context-aware responses based on uploaded content.

## Features

- *PDF Document Ingestion:* Upload PDF documents via a REST API endpoint.  
- *Dynamic Knowledge Base:* Documents are automatically chunked, embedded using a sentence-transformer model, and stored in a persistent ChromaDB vector store.  
- *AI-Powered Q&A:* A query endpoint leverages a RAG chain to retrieve relevant context from stored documents and generate concise, natural language answers.  
- *Local First:* The entire pipeline runs locally using Ollama to serve a powerful LLM (phi3) without relying on external APIs.  
- *Decoupled Architecture:* The system is built with a separate FastAPI backend for logic and an optional React frontend for user interaction.

## Tech Stack

- *Backend:* Python, FastAPI  
- *RAG Orchestration:* LangChain  
- *LLM Service:* Ollama  
- *LLM:* Microsoft Phi-3  
- *Vector Store:* ChromaDB  
- *Embedding Model:* Sentence-Transformers (all-MiniLM-L-6-v2)  
- *Frontend:* React (with Vite)

## Setup and Installation

Follow these steps to set up and run the project locally.

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)  
- [Git](https://git-scm.com/downloads)  
- [Ollama](https://ollama.com)  
- [Node.js and npm](https://nodejs.org/en/download) (for the frontend)

### 1. Clone the Repository

Clone this repository to your local machine.

```bash
git clone https://github.com/Your-GitHub-Username/Unthinkable.git
cd Unthinkable
