import re
def chunk_documents_by_sentence(
    documents: list[dict],
    chunk_size: int = 1000,
    chunk_overlap: int = 1) -> list[dict]:
    chunks = []
    chunk_id = 0

    for doc in documents:
        sentences = [
            sentence.strip()
            for sentence in re.split(r"(?<=[.!?])\s+", doc["text"])
            if sentence.strip()]

        start = 0
        while start < len(sentences):
            current_chunk = []
            current_len = 0
            end = start
            while end < len(sentences):
                sentence = sentences[end]
                additional_len = len(sentence) + (1 if current_chunk else 0)
                if current_chunk and current_len + additional_len > chunk_size:
                    break
                current_chunk.append(sentence)
                current_len += additional_len
                end += 1
            chunk_text = " ".join(current_chunk)
            chunk_metadata = doc["metadata"].copy()
            chunk_metadata["chunk_id"] = chunk_id
            chunks.append({
                "text": chunk_text,
                "metadata": chunk_metadata})
            chunk_id += 1
            if end >= len(sentences):
                break
            start = max(end - chunk_overlap, start + 1)
    return chunks
