"""
============================================================
PROJECT 08 : REAL AI AGENT

Graph

============================================================
"""

from langgraph.graph import StateGraph

from llm import llm
from state import AgentState
from tools import calculator
from prompts import PLANNER_PROMPT, RESPONSE_PROMPT

graph = StateGraph(AgentState)

# ==========================================================
# Planner Node
# ==========================================================

def planner_node(state: AgentState):

    print("\n========== Planner ==========")

    prompt = PLANNER_PROMPT.format(
        question=state["question"]
    )

    response = llm.invoke(prompt)

    print(response.content)

    # ------------------------------------------------------
    # TEMPORARY
    #
    # We are hardcoding the values for now.
    # In the next step we'll make the LLM
    # return structured output.
    # ------------------------------------------------------

    state["tool"] = "calculator"
    state["a"] = 25
    state["b"] = 75

    return state


# ==========================================================
# Tool Node
# ==========================================================

def tool_node(state: AgentState):

    print("\n========== Tool ==========")

    result = calculator.invoke(
        {
            "a": state["a"],
            "b": state["b"]
        }
    )

    print(result)

    state["result"] = result

    return state


# ==========================================================
# Response Node
# ==========================================================

def response_node(state: AgentState):

    print("\n========== Response ==========")

    prompt = RESPONSE_PROMPT.format(
        question=state["question"],
        result=state["result"]
    )

    response = llm.invoke(prompt)

    print(response.content)

    state["answer"] = response.content

    return state


# ==========================================================
# Register Nodes
# ==========================================================

graph.add_node("planner", planner_node)
graph.add_node("tool", tool_node)
graph.add_node("response", response_node)

# ==========================================================
# Flow
# ==========================================================

graph.set_entry_point("planner")

graph.add_edge("planner", "tool")
graph.add_edge("tool", "response")

graph.set_finish_point("response")

# ==========================================================
# Compile
# ==========================================================

app = graph.compile()