from mediai.ingestion.loader import load_pdf
from mediai.ingestion.normalizer import normalize_documents
documents = load_pdf(
    "data/raw/WHO.pdf",
    start_page=21,
    end_page=108,
    exclude_pages=set())

print(f"Pages loaded: {len(documents)}")
normalized_documents = normalize_documents(documents)
print(f"Normalized pages: {len(normalized_documents)}")
for document in normalized_documents:
    text = document["text"]
    print(f"Page: {document['metadata']['pdf_page']}")
    print(f"Characters: {len(text)}")
    print(f"Words: {len(text.split())}")
    print(f"First 200 characters:\n{text[:200]}")
    print(f"Last 200 characters:\n{text[-200:]}")