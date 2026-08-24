from mediai.ingestion.loader import load_pdf
from mediai.ingestion.chunker import chunk_documents_by_sentence

documents = load_pdf(
    "data/raw/WHO.pdf",
    start_page=21,
    end_page=25)

chunks = chunk_documents_by_sentence(
    documents,
    chunk_size=1000,
    chunk_overlap=1)

print(f"Documents loaded : {len(documents)}")
print(f"Chunks created   : {len(chunks)}")
for chunk in chunks:
    metadata = chunk["metadata"]
    print(f"CHUNK {metadata['chunk_id']}")
    print(f"Source      : {metadata.get('source', 'N/A')}")
    print(f"Page        : {metadata.get('page', 'N/A')}")
    print(f"Characters  : {len(chunk['text'])}")
    print("\nTEXT:")
    print(chunk["text"])