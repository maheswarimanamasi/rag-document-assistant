import streamlit as st
from query import ask_question
import os

# ✅ Move imports to top
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


st.set_page_config(
    page_title="RAGify",
    page_icon="📄",
    layout="centered"
)

st.title("📄 RAGify - Chat with your PDF")

# ✅ ONLY ONE uploader
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# ✅ SINGLE clean block
if uploaded_file is not None:
    os.makedirs("temp", exist_ok=True)

    file_path = os.path.join("temp", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # ✅ STEP 3 (correct)
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    for doc in documents:
        doc.metadata["source"]=uploaded_file.name

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = FAISS.from_documents(docs, embeddings)

    st.success("PDF processed successfully")
# ---------------------------
# Session State (Chat Memory)
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Display Chat History
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

        # 🔥 Show sources ONLY for that message
        if msg["role"] == "assistant" and msg.get("docs"):

            seen = set()
            st.markdown("**Sources:**")

            for doc in msg["docs"]:
                source = doc.metadata.get("source", "Unknown")
                page = doc.metadata.get("page", 0) + 1

                key = (source, page)

                if key not in seen:
                    seen.add(key)
                    st.markdown(f"- {source} (Page {page})")

# ---------------------------
# User Input
# ---------------------------
if prompt := st.chat_input("Ask something about the document..."):

    # 🔹 Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # 🔹 Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # 🔥 Spinner (correct placement)
    with st.spinner("🔍 Searching document..."):
        answer, docs = ask_question(prompt,db)

    # 🔹 Save assistant message WITH docs
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "docs": docs
    })

    # 🔹 Show assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

        # 🔥 Show sources ONLY if valid
        if docs:
            docs=docs[:1]
            seen = set()
            st.markdown("**Sources:**")

            for doc in docs:
                source = doc.metadata.get("source", "Unknown")
                page = doc.metadata.get("page", 0) + 1

                key = (source, page)

                if key not in seen:
                    seen.add(key)
                    st.markdown(f"- {source} (Page {page})")