# 🏥 Insurance RAG Chatbot

An AI-powered **Retrieval-Augmented Generation (RAG)** chatbot that answers insurance-related questions using policy documents and structured datasets. The application combines **FastAPI**, **Streamlit**, **Azure OpenAI**, **ChromaDB**, **BM25**, and **Cross-Encoder reranking** to provide accurate, context-aware responses while reducing hallucinations.

---

## 📌 Features

- 🔍 Hybrid Retrieval (Vector Search + BM25)
- 🧠 Azure OpenAI GPT for answer generation
- 📚 ChromaDB vector database
- 📄 Document ingestion and chunking pipeline
- 🎯 Cross-Encoder reranking for better retrieval quality
- 🛡️ Guardrails with input validation and PII detection
- 🌐 FastAPI backend
- 💻 Streamlit user interface
- 📊 Supports policy documents, FAQs, and structured CSV datasets

---

## 🏗️ Architecture

```
                  User
                    │
                    ▼
             Streamlit UI
                    │
                    ▼
               FastAPI API
                    │
                    ▼
          Input Validation &
             Guardrails
                    │
                    ▼
            Policy Detection
                    │
                    ▼
        Hybrid Retrieval Engine
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
   ChromaDB Vector Search     BM25 Search
        │                         │
        └────────────┬────────────┘
                     ▼
          Cross-Encoder Reranker
                     ▼
          Azure OpenAI GPT Model
                     ▼
               Final Response
```

---

## 📂 Project Structure

```
insurance-rag-chatbot/
│
├── backend/
│   ├── data/
│   ├── src/
│   │   ├── api/
│   │   ├── guardrails/
│   │   ├── ingestion/
│   │   ├── pipeline/
│   │   └── retrieval/
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── notebooks/
├── LICENSE
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11 |
| LLM Engine | Groq (`llama-3.3-70b-versatile`) |
| Embeddings | Local `SentenceTransformer` (`all-MiniLM-L6-v2`) |
| Vector Database | ChromaDB |
| Keyword Search | BM25 |
| Reranking | Sentence Transformers Cross-Encoder |
| Backend | FastAPI |
| Frontend | Streamlit |
| Document Processing | PyMuPDF, python-docx, pandas |
| Deployment | Streamlit Community Cloud / Hugging Face / Docker |

---

## 🚀 Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/aleem1991/Insurance-rag-chatbot.git
cd Insurance-rag-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows**
```powershell
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file in the `backend/` directory:

```env
GROQ_API_KEY=gsk_your_groq_api_key_here
GROQ_CHAT_MODEL=llama-3.3-70b-versatile
EMBEDDING_MODEL_NAME=all-MiniLM-L6-v2
```

> ⚠️ Do **not** commit your `.env` file to GitHub.

---

## 📥 Run Document Ingestion

Generate document chunks, embeddings, BM25 index, and ChromaDB collection.

```bash
cd backend

python -m src.ingestion.ingestion
```

---

## ▶️ Run the FastAPI Backend

```bash
cd backend

uvicorn src.api.main:app --reload
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 💻 Run the Streamlit UI

```bash
cd backend

streamlit run streamlit_app.py
```

Open:

```
http://localhost:8501
```

---

## 💬 Example Questions

- Does Star Comprehensive cover cataract surgery?
- What is the waiting period?
- How do I submit a reimbursement claim?
- What documents are required for cashless hospitalization?
- What are the policy exclusions?
- Is maternity covered under this policy?

---

## 📈 Retrieval Pipeline

1. User submits a query.
2. Input is validated by guardrails.
3. Policy detector identifies the relevant insurance plan.
4. Hybrid retrieval performs:
   - ChromaDB vector search
   - BM25 keyword search
5. Results are reranked using a Cross-Encoder.
6. Retrieved context is sent to Azure OpenAI GPT.
7. The model generates a grounded response.

---

## 🛡️ Guardrails

The chatbot includes:

- Input validation
- Prompt injection checks
- PII detection
- Context-grounded responses
- Hallucination reduction through retrieval

---

## 🔮 Future Improvements

- Multi-policy support
- Multi-turn conversation memory
- Authentication and user roles
- Confidence scoring
- Citation highlighting
- Kubernetes deployment
- Monitoring and observability

---

## 📸 Screenshots

Add screenshots of:

- Streamlit chat interface
- FastAPI Swagger UI
- Sample chatbot response

---

## 👨‍💻 Author

**Roshan Roy**

GitHub: https://github.com/roshanroy111999

---

## 📄 License

This project is licensed under the MIT License.
