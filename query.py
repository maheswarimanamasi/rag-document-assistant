from langchain_community.llms import Ollama

# Load LLM
llm = Ollama(model="mistral")

def ask_question(question: str, db):

    # 🔹 Step 1: retrieve docs
    docs_with_scores = db.similarity_search_with_score(question, k=2)

    docs = []
    for doc, score in docs_with_scores:
        if score < 1.5:   # adjust if needed
            docs.append(doc)

    if not docs:
        return "Not found in document", []

    # 🔹 Step 2: create context
    context = "\n\n".join([doc.page_content for doc in docs])

    # 🔹 Step 3: prompt
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

    # 🔹 Step 4: LLM call
    answer = llm.invoke(prompt).strip()

    # 🔹 Step 5: clean fallback
    if "not found" in answer.lower():
        return "Not found in document", []

    return answer, docs