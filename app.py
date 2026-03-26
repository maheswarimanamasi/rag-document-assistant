import streamlit as st
from query import ask_question

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="RAGify",
    page_icon="📄",
    layout="centered"
)

st.title("📄 RAGify - Chat with your PDF")

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
        answer, docs = ask_question(prompt)

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
            seen = set()
            st.markdown("**Sources:**")

            for doc in docs:
                source = doc.metadata.get("source", "Unknown")
                page = doc.metadata.get("page", 0) + 1

                key = (source, page)

                if key not in seen:
                    seen.add(key)
                    st.markdown(f"- {source} (Page {page})")