from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_mistralai import ChatMistralAI
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

from agent.tools import calculator, current_time
from agent.prompts import SYSTEM_PROMPT

load_dotenv()

DB_PATH = "vectorstore/chroma_db"

llm = ChatMistralAI(
    model="mistral-small-latest"
)

embeddings = MistralAIEmbeddings(
    model="mistral-embed"
)

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 3})

tools = {
    "calculator": calculator,
    "current_time": current_time
}

class AgentState(TypedDict):
    question: str
    retrieved_docs: List[str]
    answer: str

def retrieve(state):
    question = state["question"]

    docs = retriever.invoke(question)

    formatted = []

    for d in docs:
        formatted.append({
            "content": d.page_content,
            "source": d.metadata["source"],
            "chunk_id": d.metadata["chunk_id"]
        })

    return {"retrieved_docs": formatted}

def agent_node(state):
    question = state["question"].lower()

    retrieval_keywords = [
        "what is",
        "explain",
        "define",
        "rag",
        "langgraph",
        "embedding"
    ]

    if any(k in question for k in retrieval_keywords):
        return "retrieve"

    return "answer"

def answer_node(state):
    question = state["question"]
    docs = state.get("retrieved_docs", [])

    context = "\n\n".join([
        f"""
        Content: {d['content']}
        Source: {d['source']}
        Chunk: {d['chunk_id']}
        """
        for d in docs
    ])

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}

Answer clearly and cite sources used.
"""

    response = llm.invoke(prompt)

    citations = "\n".join([
        f"- {d['source']} [chunk {d['chunk_id']}]"
        for d in docs
    ])

    final_answer = f"""
{response.content}

Sources:
{citations}
"""

    return {"answer": final_answer}

workflow = StateGraph(AgentState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("answer", answer_node)

workflow.set_conditional_entry_point(
    agent_node,
    {
        "retrieve": "retrieve",
        "answer": "answer"
    }
)

workflow.add_edge("retrieve", "answer")
workflow.add_edge("answer", END)

graph = workflow.compile()
