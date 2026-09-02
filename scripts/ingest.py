from mediai.ingestion.loader import load_pdf
from mediai.ingestion.normalizer import normalize_documents
from mediai.ingestion.chunker import chunk_documents_by_sentence
from mediai.embeddings.embedder import LocalEmbeddingModel
from mediai.vectorstore.vector import VectorStore
from tqdm import tqdm

print("\n Starting PDF loading", flush=True)
documents = load_pdf("data/raw/WHO.pdf", start_page=21, end_page=100)
print(f"[1/5] PDF loading complete: {len(documents)} documents\n", flush=True)
print("[2/5] Starting text normalization", flush=True)
normalized_documents = normalize_documents(documents)
print(f"[2/5] Text normalization complete: " f"{len(normalized_documents)} documents\n", flush=True)
print("[3/5] Starting document chunking", flush=True)

chunks = chunk_documents_by_sentence(normalized_documents, chunk_size=1000, chunk_overlap=1)
print(f"[3/5] Document chunking complete: {len(chunks)} chunks\n", flush=True)
print("[4/5] Loading embedding model", flush=True)
embedding_model = LocalEmbeddingModel()

print("[4/5] Embedding model loaded successfully.", flush=True)
print("[4/5] Starting embedding generation...", flush=True)
texts = [chunk["text"] for chunk in tqdm(chunks, desc="Preparing chunk texts")]
         
embeddings = embedding_model.embed_texts(texts)
print("[4/5] Embedding generation complete.", flush=True)
print(f"Embeddings created  : {len(embeddings)}")
print(f"Embedding dimension : {len(embeddings[0])}")
print("[5/5] Starting vector store...", flush=True)
vector_store = VectorStore()
vector_store.add_documents(chunks, embeddings)

print(f"[5/5] Vector store complete: "
    f"{vector_store.count()} documents stored\n",
    flush=True)
print("Pipeline completed successfully.")