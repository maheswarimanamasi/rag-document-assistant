
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama


# 🔹 Load embedding + DB
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# 🔹 Load Mistral
llm = Ollama(model="mistral")


def ask_question(question: str):

    # 🔥 Step 1: retrieve docs
    docs_with_scores = db.similarity_search_with_score(question, k=3)
    docs_with_scores.sort(key=lambda x:x[1])
    docs = [doc for doc, _ in docs_with_scores[:2]]
    for doc, score in docs_with_scores:
        if score < 1.5:
            docs.append(doc)

    # fallback
    if not docs and docs_with_scores:
        docs = [docs_with_scores[0][0]]

    if not docs:
        return "Not found in document", []

    # 🔹 Step 2: context
    context = "\n\n".join([doc.page_content for doc in docs])

    # 🔥 Step 3: strict prompt (VERY IMPORTANT)
    prompt = f"""
You are a strict assistant.

Rules:
- Answer ONLY from the given context
- If answer is not in context → say "Not found in document"
- Give SHORT and exact answer (1–2 lines max)

Context:
{context}

Question:
{question}

Answer:
"""

    # 🔥 Step 4: LLM call
    answer = llm.invoke(prompt)

    answer = answer.strip()

    # 🔥 Step 5: remove fake sources
    if "not found" in answer.lower():
        return "Not found in document", []

    return answer, docs
