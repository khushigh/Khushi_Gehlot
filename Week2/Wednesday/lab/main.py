from typing import TypedDict

from langgraph.graph import StateGraph, END

from langchain_mistralai import ChatMistralAI

from dotenv import load_dotenv

load_dotenv()

# ==========================================
# LLM
# ==========================================

llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

# ==========================================
# STATE
# ==========================================

class GraphState(TypedDict):

    question: str
    answer: str

# ==========================================
# NODE 1
# CHECK QUESTION TYPE
# ==========================================

def router_node(state: GraphState):

    question = state["question"]

    print("\nRouting Question...")

    return state

# ==========================================
# NODE 2
# MATH NODE
# ==========================================

def math_node(state: GraphState):

    question = state["question"]

    prompt = f"Solve this math question: {question}"

    response = llm.invoke(prompt)

    state["answer"] = response.content

    return state

# ==========================================
# NODE 3
# CHAT NODE
# ==========================================

def chat_node(state: GraphState):

    question = state["question"]

    prompt = f"Answer normally: {question}"

    response = llm.invoke(prompt)

    state["answer"] = response.content

    return state

# ==========================================
# CONDITIONAL ROUTER
# ==========================================

def decide_next_node(state: GraphState):

    question = state["question"]

    math_keywords = ["add", "multiply", "+", "-", "*", "/"]

    if any(word in question.lower() for word in math_keywords):

        return "math_node"

    return "chat_node"

# ==========================================
# BUILD GRAPH
# ==========================================

graph = StateGraph(GraphState)

# add nodes
graph.add_node("router_node", router_node)

graph.add_node("math_node", math_node)

graph.add_node("chat_node", chat_node)

# entry point
graph.set_entry_point("router_node")

# conditional edge
graph.add_conditional_edges(
    "router_node",
    decide_next_node
)

# finish edges
graph.add_edge("math_node", END)

graph.add_edge("chat_node", END)

# compile graph
app = graph.compile()

# ==========================================
# RUN GRAPH
# ==========================================

while True:

    question = input("\nYou: ")

    if question == "exit":
        break

    result = app.invoke({
        "question": question,
        "answer": ""
    })

    print("\nAnswer:")
    print(result["answer"])