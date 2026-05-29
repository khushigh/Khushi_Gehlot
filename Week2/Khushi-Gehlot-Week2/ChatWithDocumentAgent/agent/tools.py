from datetime import datetime
from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression."""
    return str(eval(expression))

@tool
def current_time() -> str:
    """Get current system time."""
    return str(datetime.now())
