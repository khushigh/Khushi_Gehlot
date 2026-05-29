# Project: Build a 'chat with your documents' pipeline — load a PDF, chunk
# it, embed it, retrieve relevant chunks, and answer questions.
# 4:30–6:00 Practice: Experiment with chunk size and overlap. Compare answer
# quality. Add source citations

import uuid
from sentence_transformers import SentenceTransformer
import chromadb
from PyPDF2 import PdfReader
# from langchain import OpenAI

model = SentenceTransformer("all-MiniLM-L6-v2")

def LoadPDF(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()

    with open ("course.txt", "w", encoding="utf-8") as f:
        f.write(text)
     
    return text

def embeddAndStore(chunks):
    c = chromadb.PersistentClient()
    collection = c.get_or_create_collection(name="my_collection")

    embeddings = model.encode(chunks)

    collection.add(
        documents = chunks,
        embeddings = embeddings.tolist(),
        ids=[str(uuid.uuid4()) for _ in chunks],
        metadatas=[
            {"source": f"chunk_{i}"}
            for i in range(len(chunks))
        ]
    )

def answerQuestion(question):
    pass

def chunk_text(text, chunk_size=300, overlap=50):

    # with open("course.txt", "r", encoding="utf-8") as f:
    #     text = f.read()

    words = text.split()

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

def retrieve():
    c = chromadb.PersistentClient()
    collection = c.get_or_create_collection(name="my_collection")

    while True:
        query = input("Enter a query: ")
        if(query == "exit"):
            break

        query_embedding = model.encode(query)
        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=1
        )
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        print("\nTop Relevant Chunks:\n")

        for i, (doc, meta) in enumerate(zip(documents, metadatas)):
            print(f"Result {i+1}")
            print(f"Source: {meta['source']}")
            print(doc[:400])
            print("-" * 50)

def main():
    # text = LoadPDF("course.pdf")
    # chunks = chunk_text(text)
    # embeddAndStore(chunks)
    retrieve()


if __name__ == "__main__":
    main()



#decreasing chunk size and increasing overlap will increase the number of chunks, which will increase the chances of retrieving relevant information, but it will also increase the storage requirements and retrieval time. 

            