import re
def chunk_documents_by_sentence(
    documents: list[dict],
    chunk_size: int = 1000,
    chunk_overlap: int = 1) -> list[dict]:
    chunks = []
    chunk_id = 0

    for doc in documents:
        sentences = re.split(r"(?<=[.!?]) +", doc["text"])
        current_chunk = []
        current_len = 0
        i = 0
        while i < len(sentences):
            sentence = sentences[i]
            if current_len + len(sentence) > chunk_size and current_chunk:
                chunk_text = " ".join(current_chunk)
                chunk_metadata = doc["metadata"].copy()
                chunk_metadata["chunk_id"] = chunk_id
                chunks.append({
                    "text": chunk_text,
                    "metadata": chunk_metadata})

                chunk_id += 1
                i = max(i - chunk_overlap, 0)
                current_chunk = []
                current_len = 0
                continue

            current_chunk.append(sentence)
            current_len += len(sentence) + 1
            i += 1
        if current_chunk:
            chunk_metadata = doc["metadata"].copy()
            chunk_metadata["chunk_id"] = chunk_id
            chunks.append({
                "text": " ".join(current_chunk),
                "metadata": chunk_metadata})
            chunk_id += 1
    return chunks