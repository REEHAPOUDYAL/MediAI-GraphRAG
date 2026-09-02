import chromadb
class VectorStore:
    def __init__(self, persist_directory: str = "data/vectorstore"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="mediai_documents",
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(
        self,
        chunks: list[dict],
        embeddings: list[list[float]]
    ) -> None:
        self.collection.add(
            ids=[str(chunk["metadata"]["chunk_id"]) for chunk in chunks],
            embeddings=embeddings,
            documents=[chunk["text"] for chunk in chunks],
            metadatas=[chunk["metadata"] for chunk in chunks]
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 5
    ) -> dict:
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

    def count(self) -> int:
        return self.collection.count()