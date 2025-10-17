import os
import shutil
import datetime
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

# --- LangChain Imports ---
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- APP INITIALIZATION ---
app = FastAPI(
    title="Unthinkable RAG API",
    description="An API for a Retrieval-Augmented Generation system.",
    version="1.0.0",
)

# --- GLOBAL VARIABLES & CONFIGURATION ---
VECTOR_STORE_PATH = "vector_store"
# This now points to your local, manually downloaded model folder
embedding_model = SentenceTransformerEmbeddings(model_name="./local_model") 
llm = Ollama(model="phi3")

# --- DATA MODELS ---
class QueryRequest(BaseModel):
    question: str

# --- RAG CHAIN LOGIC ---
def get_rag_chain():
    """
    Initializes and returns the RAG chain.
    """
    vector_store = Chroma(persist_directory=VECTOR_STORE_PATH, embedding_function=embedding_model)
    retriever = vector_store.as_retriever()
    
    template = """
    You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Use three sentences maximum and keep the answer concise.
    Question: {question} 
    Context: {context} 
    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

# --- DOCUMENT PROCESSING AND STORAGE LOGIC ---
def process_and_store_document(file_path: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=VECTOR_STORE_PATH
    )
    return len(chunks)

# --- API ENDPOINTS ---
@app.get("/")
def read_root():
    return {"message": "API is running successfully!"}

@app.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    temp_dir = "temp_docs"
    os.makedirs(temp_dir, exist_ok=True)
    temp_file_path = os.path.join(temp_dir, file.filename)
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        num_chunks = process_and_store_document(temp_file_path)
        return {"status": "success", "filename": file.filename, "chunks_stored": num_chunks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    finally:
        file.file.close()
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

@app.post("/query")
async def handle_query(query: QueryRequest):
    """
    Endpoint to handle user queries and return a synthesized answer.
    """
    try:
        print(f"\n[{datetime.datetime.now()}] --- Query received: '{query.question}'")

        print(f"[{datetime.datetime.now()}] --- Initializing RAG chain...")
        rag_chain = get_rag_chain()
        print(f"[{datetime.datetime.now()}] --- RAG chain initialized.")

        print(f"[{datetime.datetime.now()}] --- Invoking RAG chain...")
        answer = rag_chain.invoke(query.question)
        print(f"[{datetime.datetime.now()}] --- RAG chain invocation complete.")

        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during query processing: {str(e)}")