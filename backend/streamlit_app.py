import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000/chat")

st.set_page_config(
    page_title="Insurance RAG Assistant",
    page_icon="🏥",
    layout="wide",
)

st.title("🏥 Insurance RAG Assistant")
st.caption("Ask questions about insurance policies.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            sources = message.get("sources", [])

            if sources:

                with st.expander("📄 Sources"):

                    for source in sources:

                        st.write(
                            f"**{source['source']}**"
                        )

                        if source["section"]:

                            st.caption(
                                source["section"]
                            )

# Chat input
question = st.chat_input(
    "Ask a question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching policy documents..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=10,
                )

                if response.status_code == 200:
                    result = response.json()
                    answer = result.get("answer", "No response text.")
                    sources = result.get("sources", [])
                else:
                    raise ConnectionError(f"HTTP {response.status_code}")
            except Exception:
                # Direct fallback for single-process cloud deployment (e.g. Streamlit Cloud / HF Spaces)
                try:
                    from src.guardrails.validators import check_input
                    from src.pipeline.rag_pipeline import RAGPipeline

                    if "rag_engine" not in st.session_state:
                        st.session_state.rag_engine = RAGPipeline()

                    is_safe, reason, msg = check_input(question)
                    if not is_safe:
                        answer = msg
                        sources = []
                    else:
                        res = st.session_state.rag_engine.ask(question)
                        answer = res["answer"]
                        sources = res["sources"]
                except Exception as direct_err:
                    answer = f"⚠️ Error generating response: {direct_err}"
                    sources = []

            st.markdown(answer)

            if sources:

                with st.expander("📄 Sources"):

                    for source in sources:

                        st.write(
                            f"**{source['source']}**"
                        )

                        if source["section"]:

                            st.caption(
                                source["section"]
                            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources,
        }
    )