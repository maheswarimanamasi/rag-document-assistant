RAG-based SOP Assistant

A Retrieval-Augmented Generation (RAG) system that answers questions from PDF documents using a vector database and an LLM.

Features

- Ask questions from a PDF document
- Uses FAISS vector database for semantic search
- FastAPI backend for API handling
- Streamlit chat interface for user interaction
- Context-based answers from document

Project Structure

production_rag/

- src/ → Backend logic (RAG pipeline)
- ui/ → Streamlit user interface
- data/ → PDF documents used for retrieval

Tech Stack

- Python
- LangChain
- FAISS
- FastAPI
- Streamlit

Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/rag-document-assistant.git

Go to the project folder

cd rag-document-assistant

Install dependencies

pip install -r requirements.txt

Run the Project

Step 1: Create the vector database

python production_rag/src/ingest.py

Step 2: Start the API server

uvicorn production_rag.src.api:app --reload

Step 3: Run the Streamlit UI

streamlit run production_rag/ui/app.py

Example Question

how many sick leave days are allowed

Output

The answer is 10 sick leave days per year.