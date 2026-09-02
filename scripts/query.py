from mediai.embeddings.embedder import LocalEmbeddingModel
from mediai.vectorstore.vector import VectorStore

embedding_model = LocalEmbeddingModel()
vector_store = VectorStore()
query = input("\nEnter your question: ").strip()
query_embedding = embedding_model.embed_texts([query])[0]

results = vector_store.search(query_embedding=query_embedding, top_k=5)
print("\nTop relevant chunks:\n")

for i in range(len(results["documents"][0])):
    print(f"Result {i + 1}")
    print(f"Distance: {results['distances'][0][i]}")
    print(f"Metadata: {results['metadatas'][0][i]}")
    print(f"Text: {results['documents'][0][i]}")
    print()