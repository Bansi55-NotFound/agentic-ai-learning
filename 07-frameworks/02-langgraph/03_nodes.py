"""
============================================================
PROJECT 08 : LANGGRAPH

Example 3 : Understanding Nodes

Goal:
Learn how multiple nodes work and how State
travels from one node to another.

============================================================
"""

from typing import TypedDict
from langgraph.graph import StateGraph

# ==========================================================
# Step 1 : Define State
# ==========================================================
# This is the shared data that every node can access.
# ==========================================================

class State(TypedDict):
    message: str
    step: int


# ==========================================================
# Step 2 : Create Graph
# ==========================================================

graph = StateGraph(State)


# ==========================================================
# Step 3 : Planner Node
# ==========================================================
# Reads the state
# Updates it
# Returns it
# ==========================================================

def planner_node(state: State):

    print("\n========== Planner Node ==========")

    print("Message :", state["message"])
    print("Step :", state["step"])

    state["step"] += 1

    print("Planner updated Step to :", state["step"])

    return state


# ==========================================================
# Step 4 : Executor Node
# ==========================================================

def executor_node(state: State):

    print("\n========== Executor Node ==========")

    print("Message :", state["message"])
    print("Step :", state["step"])

    state["step"] += 1

    print("Executor updated Step to :", state["step"])

    return state


# ==========================================================
# Step 5 : Reflection Node
# ==========================================================

def reflection_node(state: State):

    print("\n========== Reflection Node ==========")

    print("Message :", state["message"])
    print("Step :", state["step"])

    state["step"] += 1

    print("Reflection updated Step to :", state["step"])

    return state


# ==========================================================
# Step 6 : Register Nodes
# ==========================================================

graph.add_node("planner", planner_node)
graph.add_node("executor", executor_node)
graph.add_node("reflection", reflection_node)


# ==========================================================
# Step 7 : Connect Nodes
# ==========================================================
#
# START
#   |
#   v
# planner
#   |
#   v
# executor
#   |
#   v
# reflection
#   |
#   v
# END
#
# ==========================================================

graph.set_entry_point("planner")

graph.add_edge("planner", "executor")
graph.add_edge("executor", "reflection")

graph.set_finish_point("reflection")


# ==========================================================
# Step 8 : Compile Graph
# ==========================================================

app = graph.compile()


# ==========================================================
# Step 9 : Initial State
# ==========================================================

initial_state = {
    "message": "Learn LangGraph",
    "step": 1
}


# ==========================================================
# Step 10 : Run Graph
# ==========================================================

app.invoke(initial_state)