# ============================================================
# Project 15 - Multi-Agent Research Assistant
#
# File: workflow.py
#
# Purpose:
# Define the LangGraph workflow connecting multiple agents.
# ============================================================

from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents import (
    planner_agent,
    writer_agent,
    reviewer_agent
)


# ============================================================
# Workflow State
# ============================================================

class ResearchState(TypedDict):
    topic: str
    plan: str
    report: str
    final_report: str


# ============================================================
# Planner Node
# ============================================================

def planner_node(state: ResearchState):

    print("\n🧠 Planner Agent Running...\n")

    plan = planner_agent.invoke(
        {
            "topic": state["topic"]
        }
    )

    return {
        "plan": plan
    }


# ============================================================
# Writer Node
# ============================================================

def writer_node(state: ResearchState):

    print("\n✍️ Writer Agent Running...\n")

    report = writer_agent.invoke(
        {
            "plan": state["plan"]
        }
    )

    return {
        "report": report
    }


# ============================================================
# Reviewer Node
# ============================================================

def reviewer_node(state: ResearchState):

    print("\n✅ Reviewer Agent Running...\n")

    final_report = reviewer_agent.invoke(
        {
            "report": state["report"]
        }
    )

    return {
        "final_report": final_report
    }


# ============================================================
# Build Workflow
# ============================================================

workflow = StateGraph(ResearchState)

workflow.add_node("planner", planner_node)

workflow.add_node("writer", writer_node)

workflow.add_node("reviewer", reviewer_node)


# ============================================================
# Connect Nodes
# ============================================================

workflow.set_entry_point("planner")

workflow.add_edge("planner", "writer")

workflow.add_edge("writer", "reviewer")

workflow.add_edge("reviewer", END)


# ============================================================
# Compile Workflow
# ============================================================

graph = workflow.compile()