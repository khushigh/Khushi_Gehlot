from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DOCS_PATH = "ingest/documents"
DB_PATH = "vectorstore/chroma_db"

documents = []

for file in Path(DOCS_PATH).glob("*.txt"):
    loader = TextLoader(str(file))
    docs = loader.load()

    for d in docs:
        d.metadata["source"] = file.name

    documents.extend(docs)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

for i, chunk in enumerate(chunks):
    chunk.metadata["chunk_id"] = i

embeddings = MistralAIEmbeddings(
    model="mistral-embed"
)

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

db.persist()

print("Documents ingested successfully.")
