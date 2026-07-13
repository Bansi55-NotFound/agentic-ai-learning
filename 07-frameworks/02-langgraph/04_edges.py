"""
============================================================
PROJECT 08 : LANGGRAPH

Example 4 : Understanding Edges

Goal:
Learn how nodes are connected using edges.

============================================================
"""

from typing import TypedDict
from langgraph.graph import StateGraph

# ==========================================================
# Step 1 : Define State
# ==========================================================

class State(TypedDict):
    message: str

# ==========================================================
# Step 2 : Create Graph
# ==========================================================

graph = StateGraph(State)

# ==========================================================
# Step 3 : Nodes
# ==========================================================

def planner_node(state: State):

    print("Planner Node")

    return state


def executor_node(state: State):

    print("Executor Node")

    return state


def reflection_node(state: State):

    print("Reflection Node")

    return state

# ==========================================================
# Step 4 : Register Nodes
# ==========================================================

graph.add_node("planner", planner_node)
graph.add_node("executor", executor_node)
graph.add_node("reflection", reflection_node)

# ==========================================================
# Step 5 : Entry Point
# ==========================================================

graph.set_entry_point("planner")

# ==========================================================
# Step 6 : Edges
# ==========================================================

graph.add_edge("planner", "executor")
graph.add_edge("executor", "reflection")

# ==========================================================
# Step 7 : Finish Point
# ==========================================================

graph.set_finish_point("reflection")

# ==========================================================
# Step 8 : Compile
# ==========================================================

app = graph.compile()

# ==========================================================
# Step 9 : Run
# ==========================================================

app.invoke(
    {
        "message": "Hello"
    }
)