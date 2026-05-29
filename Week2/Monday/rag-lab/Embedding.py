from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

# str1 = "dog"
# str2 = "puppy"
# str3 = "tax"
# embedding1 = model.encode(str1)
# embedding2 = model.encode(str2)     
# embedding3 = model.encode(str3)

# print(cosine_similarity([embedding1], [embedding2]))
# print(cosine_similarity([embedding1], [embedding3]))


words = ["dog", "tax"]
word_embeddings = model.encode(words)

while True:
    query = input("Enter a word: ")
    query_embedding = model.encode(query)

    if(query == "exit"):
        break

    similarities = cosine_similarity([query_embedding], word_embeddings)
    most_similar_index = similarities.argmax()
    most_similar_word = words[most_similar_index]
    print(f"The most similar word to '{query}' is '{most_similar_word}' with a similarity score of {similarities[0][most_similar_index]:.4f}")