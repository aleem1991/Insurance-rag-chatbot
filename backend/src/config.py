import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

load_dotenv(BASE_DIR / ".env")
load_dotenv()

# Groq LLM Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_CHAT_MODEL = os.getenv("GROQ_CHAT_MODEL", "llama-3.3-70b-versatile")

# Embeddings (Local SentenceTransformer default - zero API key required)
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")

# Azure OpenAI (Optional)
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

CHAT_MODEL = os.getenv("CHAT_MODEL", GROQ_CHAT_MODEL)
EMBED_MODEL = os.getenv("EMBED_MODEL", EMBEDDING_MODEL_NAME)

# AWS
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

# S3
S3_BUCKET = os.getenv("S3_BUCKET")

# ChromaDB
default_chroma = DATA_DIR / "chromadb"
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", str(default_chroma))

# Tenant
TENANT_ID = os.getenv("TENANT_ID", "star-health")