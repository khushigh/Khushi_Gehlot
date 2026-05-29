
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

strings = ["dog is a pet", "cat is a pet", "tax is a financial charge"]
embeddings = model.encode(strings)

# while True:
#     query = input("Enter a query: ")
#     query_embedding = model.encode(query)

#     if(query == "exit"):
#         break

#     similarities = cosine_similarity([query_embedding], embeddings)
#     most_similar_index = similarities.argmax()
#     most_similar_string = strings[most_similar_index]
#     print(f"The most similar string to '{query}' is '{most_similar_string}' with a similarity score of {similarities[0][most_similar_index]:.4f}")