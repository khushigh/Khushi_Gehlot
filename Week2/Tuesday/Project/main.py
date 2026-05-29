from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_mistralai import ChatMistralAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


loader = PyPDFLoader("Project/ML.pdf")

documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

docs = splitter.split_documents(documents)


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="./chroma_db"
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    """
Answer the question ONLY using the provided context.

Context:
{context}

Question:
{question}
"""
)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        exit()

    retrieved_docs = retriever.invoke(question)

    context = "\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    answer = chain.invoke({
        "context": context,
        "question": question
    })

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    for i, doc in enumerate(retrieved_docs):

        print(f"\nSource {i+1}")
        print(doc.metadata)