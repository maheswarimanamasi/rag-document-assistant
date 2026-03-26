📄 RAGify – Ask Your PDF

A Retrieval-Augmented Generation (RAG) application that lets users ask questions from a PDF and get accurate, concise answers with citations (source + page number).

---

🚀 Features

- 🔍 Ask questions directly from PDF documents
- 📌 Returns exact answers (no unnecessary text)
- 📄 Displays source file and page number
- ⚡ Fast search using FAISS vector database
- 💬 Chat-style interface with Streamlit
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

⚙️ Installation

git clone https://github.com/maheswarimanamasi/rag-document-assistant.git
cd rag-document-assistant
pip install -r requirements.txt

---

▶️ How to Run

Step 1: Create Vector Database

python ingest.py

Step 2: Start Application

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


⚠️ Limitations

- Works best with structured PDFs
- Not optimized for very large documents
- Accuracy depends on document quality