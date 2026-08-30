from mediai.ingestion.loader import load_pdf
from mediai.ingestion.normalizer import normalize_documents
from mediai.ingestion.chunker import chunk_documents_by_sentence
from mediai.embeddings.embedder import LocalEmbeddingModel


documents = load_pdf("data/raw/WHO.pdf", start_page=21, end_page=100)
normalized_documents = normalize_documents(documents)
chunks = chunk_documents_by_sentence(normalized_documents,chunk_size=1000, chunk_overlap=1)
print(f"Documents loaded: {len(documents)}")
print(f"Documents normalized: {len(normalized_documents)}")
print(f"Chunks created: {len(chunks)}")

embedding_model = LocalEmbeddingModel()
texts = [chunk["text"] for chunk in chunks]
embeddings = embedding_model.embed_texts(texts)
print(f"Embeddings created   : {len(embeddings)}")
print(f"Embedding dimension  : {len(embeddings[0])}")

for chunk, embedding in zip(chunks[:5], embeddings[:5]):
    metadata = chunk["metadata"]
    print(f"CHUNK {metadata['chunk_id']}")
    print(f"Source      : {metadata.get('source', 'N/A')}")
    print(f"PDF Page    : {metadata.get('pdf_page', 'N/A')}")
    print(f"Characters  : {len(chunk['text'])}")
    print(f"Embedding   : {len(embedding)} dimensions")
    print("\nTEXT:")
    print(chunk["text"])
