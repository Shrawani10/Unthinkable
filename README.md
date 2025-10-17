# Unthinkable: Knowledge-base Search Engine

## Description
This project is a knowledge-base search engine that allows users to search across multiple documents and receive synthesized answers. [cite_start]It uses a Retrieval-Augmented Generation (RAG) pipeline powered by a local Large Language Model (LLM) to provide accurate, context-aware responses. [cite: 3]

## Features
* **Document Ingestion:** Upload PDF documents via an API endpoint.
* **Vector Storage:** Documents are chunked, embedded, and stored in a persistent ChromaDB vector store.
* **Question Answering:** A query endpoint leverages a RAG chain to retrieve relevant context and generate answers using a local LLM (Ollama with Phi-3).
* **API Interface:** The entire system is exposed via a FastAPI backend.

## Tech Stack
* **Backend:** FastAPI
* **RAG Orchestration:** LangChain
* **LLM:** Ollama (with `phi3`)
* **Vector Store:** ChromaDB
* **Embedding Model:** Sentence-Transformers (`all-MiniLM-L-6-v2`)

## Setup and Installation

**1. Clone the Repository:**
```bash
git clone [https://github.com//unthinkable.git](https://github.com/Your-GitHub-Username/unthinkable.git)
cd unthinkable
