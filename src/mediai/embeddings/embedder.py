from sentence_transformers import SentenceTransformer
class LocalEmbeddingModel:
    def __init__(self, model: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model)

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return embeddings.tolist()