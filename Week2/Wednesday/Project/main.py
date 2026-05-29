from typing import TypedDict, Annotated

from dotenv import load_dotenv

from langgraph.graph import StateGraph, END

from langchain_mistralai import ChatMistralAI

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

class AgentState(TypedDict):

    question: str
    thought: str
    tool_result: str
    answer: str

# ==========================================
# TOOL
# ==========================================

def calculator_tool(expression):

    try:
        result = eval(expression)

        return str(result)

    except:

        return "Invalid math expression"

# ==========================================
# AGENT NODE
# ==========================================

def agent_node(state: AgentState):

    question = state["question"]

    tool_result = state.get("tool_result", "")

    prompt = f"""
You are an AI agent.

Question:
{question}

Previous Tool Result:
{tool_result}

If a calculator is needed,
respond ONLY like this:

CALCULATE: 45 * 12

Otherwise give final answer like this:

FINAL ANSWER: answer here
"""

    response = llm.invoke(prompt)

    output = response.content

    print("\nAgent Thinking:")
    print(output)

    state["thought"] = output

    return state

# ==========================================
# TOOL NODE
# ==========================================

def tool_node(state: AgentState):

    thought = state["thought"]

    expression = thought.replace("CALCULATE:", "").strip()

    result = calculator_tool(expression)

    print("\nTool Result:")
    print(result)

    state["tool_result"] = result

    return state

# ==========================================
# ROUTER
# ==========================================

def router(state: AgentState):

    thought = state["thought"]

    if thought.startswith("CALCULATE:"):

        return "tool_node"

    return "final_node"

# ==========================================
# FINAL NODE
# ==========================================

def final_node(state: AgentState):

    thought = state["thought"]

    answer = thought.replace(
        "FINAL ANSWER:",
        ""
    ).strip()

    state["answer"] = answer

    return state

# ==========================================
# BUILD GRAPH
# ==========================================

graph = StateGraph(AgentState)

graph.add_node("agent_node", agent_node)

graph.add_node("tool_node", tool_node)

graph.add_node("final_node", final_node)

# entry point
graph.set_entry_point("agent_node")

# conditional routing
graph.add_conditional_edges(
    "agent_node",
    router
)

# LOOP BACK
graph.add_edge("tool_node", "agent_node")

# finish
graph.add_edge("final_node", END)

# compile
app = graph.compile()

# ==========================================
# RUN
# ==========================================

while True:

    question = input("\nYou: ")

    if question == "exit":
        break

    result = app.invoke({

        "question": question,

        "thought": "",

        "tool_result": "",

        "answer": ""
    })

    print("\nFinal Answer:")
    print(result["answer"])