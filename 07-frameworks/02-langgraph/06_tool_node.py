"""
============================================================
PROJECT 08 : LANGGRAPH

Example 6 : Tool Node

============================================================
"""

from typing import TypedDict

from langgraph.graph import StateGraph
from langchain_core.tools import tool

# ==========================================================
# Step 1 : Tool
# ==========================================================

@tool
def calculator(a: int, b: int) -> int:
    """
    Add two numbers.
    """

    return a + b


# ==========================================================
# Step 2 : State
# ==========================================================

class State(TypedDict):
    result: int


# ==========================================================
# Step 3 : Graph
# ==========================================================

graph = StateGraph(State)


# ==========================================================
# Step 4 : Tool Node
# ==========================================================

def tool_node(state: State):

    result = calculator.invoke(
        {
            "a": 20,
            "b": 80
        }
    )

    print("Tool Result :", result)

    state["result"] = result

    return state


# ==========================================================
# Step 5 : Register Node
# ==========================================================

graph.add_node(
    "tool",
    tool_node
)

graph.set_entry_point("tool")

graph.set_finish_point("tool")


# ==========================================================
# Step 6 : Compile
# ==========================================================

app = graph.compile()


# ==========================================================
# Step 7 : Run
# ==========================================================

app.invoke(
    {
        "result": 0
    }
)