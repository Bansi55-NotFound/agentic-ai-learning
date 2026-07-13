"""
============================================================
PROJECT 08 : LANGGRAPH

Example 2 : Understanding State

Goal:
Learn what State is and how it flows through the graph.

============================================================
"""

from typing import TypedDict
from langgraph.graph import StateGraph

# ==========================================================
# Step 1 : Define State
# ==========================================================
# State is a shared dictionary that travels through
# every node in the graph.
#
# Every node can:
# 1. Read values from the state
# 2. Add new values
# 3. Update existing values
# 4. Return the updated state
# ==========================================================

class State(TypedDict):
    message: str


# ==========================================================
# Step 2 : Create Graph
# ==========================================================

graph = StateGraph(State)


# ==========================================================
# Step 3 : Create Node
# ==========================================================
# Every node receives the current state.
# Here we simply print it.
# ==========================================================

def hello_node(state: State):

    print("=" * 50)
    print("Current State Received")
    print("=" * 50)

    print(state)

    print("\nMessage inside State:")
    print(state["message"])

    # Return the same state
    return state


# ==========================================================
# Step 4 : Register Node
# ==========================================================

graph.add_node(
    "hello",
    hello_node
)


# ==========================================================
# Step 5 : Define Graph Flow
# ==========================================================
#
# START
#   |
#   v
# hello
#   |
#   v
# END
#
# ==========================================================

graph.set_entry_point("hello")
graph.set_finish_point("hello")


# ==========================================================
# Step 6 : Compile Graph
# ==========================================================

app = graph.compile()


# ==========================================================
# Step 7 : Initial State
# ==========================================================
#
# The dictionary below becomes the initial state.
#
# LangGraph automatically passes it to the first node.
#
# ==========================================================

initial_state = {
    "message": "Hello LangGraph!"
}


# ==========================================================
# Step 8 : Execute Graph
# ==========================================================

app.invoke(initial_state)