"""
============================================================
PROJECT 08 : LANGGRAPH

Example 8 : Multi-Agent

Goal:
Understand how multiple agents work together.

============================================================
"""

from typing import TypedDict
from langgraph.graph import StateGraph


# ==========================================================
# Step 1 : State
# ==========================================================

class State(TypedDict):
    task: str


# ==========================================================
# Step 2 : Graph
# ==========================================================

graph = StateGraph(State)


# ==========================================================
# Step 3 : Planner Agent
# ==========================================================

def planner_agent(state: State):

    print("Planner Agent")
    print("Task :", state["task"])

    return state


# ==========================================================
# Step 4 : Research Agent
# ==========================================================

def research_agent(state: State):

    print("Research Agent")

    return state


# ==========================================================
# Step 5 : Writer Agent
# ==========================================================

def writer_agent(state: State):

    print("Writer Agent")

    return state


# ==========================================================
# Step 6 : Register Agents
# ==========================================================

graph.add_node("planner", planner_agent)
graph.add_node("research", research_agent)
graph.add_node("writer", writer_agent)


# ==========================================================
# Step 7 : Connect Agents
# ==========================================================

graph.set_entry_point("planner")

graph.add_edge("planner", "research")
graph.add_edge("research", "writer")

graph.set_finish_point("writer")


# ==========================================================
# Step 8 : Compile
# ==========================================================

app = graph.compile()


# ==========================================================
# Step 9 : Run
# ==========================================================

app.invoke(
    {
        "task": "Write an article about AI"
    }
)