📄 RAGify – Ask Your PDF

A Retrieval-Augmented Generation (RAG) application that lets users ask questions from a PDF and get accurate, concise answers with citations (source + page number).

---

🚀 Features
- 🔍 chat with pdf using RAG
- 📌 Returns exact answers with page citations (no unnecessary text)
- 📄 Displays source file and page number
- ⚡ Fast search using FAISS vector database
- 💬 Chat-style interface with Streamlit
-    Local LLM using Mistral (ollama)
- 🚫 Handles irrelevant queries → "Not found in document"

---

🧠 How It Works

1. Load PDF document
2. Split into smaller chunks
3. Convert chunks into embeddings
4. Store embeddings in FAISS
5. Convert user query into embedding
6. Retrieve relevant chunks
7. Generate answer using LLM

---

🛠️ Tech Stack

- Python
- LangChain
- FAISS
- Sentence Transformers
- Streamlit
- HuggingFace Embeddings
- Ollama (Mistral)

---

📂 Project Structure

RAG_PROJECT/
│
├── app.py              # Streamlit UI
├── query.py            # RAG pipeline logic
├── ingest.py           # PDF → FAISS indexing
├── requirements.txt
├── README.md
│
├── data/
│   └── policy.pdf
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl

---


▶️ How to Run

## 🚀 How to Run

### 1. Clone the repo
git clone https://github.com/your-username/rag-document-assistant.git
cd rag-document-assistant

### 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run ingestion
python ingest.py

### 5. Start app
streamlit run app.py
---

💡 Example Queries

- What are working hours?
- How many sick leave days are allowed?
- What is maternity leave policy?
- Who is the CEO? (should return Not found)

---

📸 Screenshots

## 📸 Screenshots

### 🖥️ Application UI
![UI](assets/ui.png)

### 📄 Answer with Citations
![Answer](assets/answer.png)

## 🎥 Demo

![Demo](assets/demo.mp4)


⚠️ Limitations

- Works best with structured PDFs
- Not optimized for very large documents
- Accuracy depends on document quality