from pathlib import Path
from pypdf import PdfReader

def load_pdf(
    file_path: str,
    start_page: int = 1,
    end_page: int | None = None,
    exclude_pages: set[int] | None = None):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    reader = PdfReader(path)
    total_pages = len(reader.pages)
    start = max(start_page - 1, 0)
    end = min(end_page or total_pages, total_pages)
    excluded = exclude_pages or {93, 94, 95, 96}
    documents = []

    for page_number in range(start, end):
        pdf_page = page_number + 1
        if pdf_page in excluded:
            continue
        text = reader.pages[page_number].extract_text() or ""
        if text.strip():
            documents.append({
                "text": text.strip(),
                "metadata": {
                    "source": path.name,
                    "pdf_page": pdf_page}})

    return documents