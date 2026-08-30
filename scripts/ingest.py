from mediai.ingestion.loader import load_pdf
from mediai.ingestion.normalizer import normalize_documents
from mediai.ingestion.chunker import chunk_documents_by_sentence
from mediai.embeddings.embedder import LocalEmbeddingModel

print("Start", flush=True)
print("Loading PDF...", flush=True)
documents = load_pdf(
    "data/raw/WHO.pdf",
    start_page=21,
    end_page=100)
print(f"PDF loaded: {len(documents)} documents", flush=True)
print("Normalizing...", flush=True)
normalized_documents = normalize_documents(documents)
print(f"Normalized: {len(normalized_documents)} documents", flush=True)

print("Chunking...", flush=True)
chunks = chunk_documents_by_sentence(
    normalized_documents,
    chunk_size=1000,
    chunk_overlap=1
)
print(f"Chunks created: {len(chunks)}", flush=True)

print("Loading embedding model...", flush=True)
embedding_model = LocalEmbeddingModel()
print("Embedding model loaded!", flush=True)

print("Creating embeddings...", flush=True)
texts = [chunk["text"] for chunk in chunks]
embeddings = embedding_model.embed_texts(texts)
print(f"Embeddings created: {len(embeddings)}", flush=True)
print(f"Embedding dimension: {len(embeddings[0])}", flush=True)