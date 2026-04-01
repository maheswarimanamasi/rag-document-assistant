from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load PDF
loader = PyPDFLoader("data/policy.pdf")
documents = loader.load()

# Clean metadata
for doc in documents:
    doc.metadata["source"] = "policy.pdf"

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

docs = text_splitter.split_documents(documents)
print("Total chunks created :",len(docs))

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create FAISS index
db = FAISS.from_documents(docs, embeddings)

# Save
db.save_local("faiss_index")

print("✅ FAISS index created successfully")