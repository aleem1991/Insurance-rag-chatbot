from sentence_transformers import SentenceTransformer
from src.config import (
    EMBEDDING_MODEL_NAME,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    EMBED_MODEL,
)

_embedder = None

def get_embedder():
    global _embedder
    if _embedder is None:
        if AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT and "your_key" not in AZURE_OPENAI_API_KEY:
            from openai import AzureOpenAI
            _embedder = ("azure", AzureOpenAI(
                api_key=AZURE_OPENAI_API_KEY,
                azure_endpoint=AZURE_OPENAI_ENDPOINT,
                api_version=AZURE_OPENAI_API_VERSION,
            ))
        else:
            _embedder = ("local", SentenceTransformer(EMBEDDING_MODEL_NAME))
    return _embedder


def generate_embedding(text: str):
    """
    Generate an embedding for a single text chunk.
    """
    embedder_type, embedder = get_embedder()
    if embedder_type == "azure":
        response = embedder.embeddings.create(
            model=EMBED_MODEL,
            input=text,
        )
        return response.data[0].embedding
    else:
        embedding = embedder.encode(text, normalize_embeddings=True)
        return embedding.tolist()


def generate_embeddings(chunks):
    """
    Generate embeddings for all chunks.
    """
    embedder_type, embedder = get_embedder()
    if embedder_type == "local":
        texts = [chunk["text"] for chunk in chunks]
        embeddings = embedder.encode(texts, normalize_embeddings=True, show_progress_bar=True)
        for chunk, emb in zip(chunks, embeddings):
            chunk["embedding"] = emb.tolist()
    else:
        for chunk in chunks:
            chunk["embedding"] = generate_embedding(chunk["text"])

    return chunks