import re
def normalize_text(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" *\n *", "\n", text)
    return text.strip()

def normalize_documents(documents: list[dict]) -> list[dict]:
    normalized_documents = []
    for document in documents:
        normalized_text = normalize_text(document["text"])
        if not normalized_text:
            continue
        normalized_documents.append(
            {
                "text": normalized_text,
                "metadata": document["metadata"].copy()
            }
        )
    return normalized_documents