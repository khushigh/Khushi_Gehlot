# Lab: Generate embeddings for text. Store them in a vector store (Chroma
# / FAISS). Run similarity search queries.

from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
c = chromadb.Client()
collection = c.get_or_create_collection(name="my_collection")
strings = ["dog is a pet", "tax is a financial charge"]
embeddings = model.encode(strings)

collection.add(
    documents = strings,
    embeddings = embeddings.tolist(),
    ids = [f"doc{i}" for i in range(len(embeddings))]
)
while True:
    query = input("Enter a query: ")
    if(query == "exit"):
        break

    query_embedding = model.encode(query)
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=1
    )
    print("\nClosest match:")
    print(results)
    print()
