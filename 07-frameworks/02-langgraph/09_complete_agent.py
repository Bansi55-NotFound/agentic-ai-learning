"""
============================================================
PROJECT 08 : LANGGRAPH

Example 9 : Complete AI Agent

Goal:
Combine all LangGraph concepts together.

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

    question: str

    result: int


# ==========================================================
# Step 3 : Graph
# ==========================================================

graph = StateGraph(State)

# ==========================================================
# Step 4 : Planner Node
# ==========================================================

def planner_node(state: State):

    print("\n========== Planner ==========")

    print("Question :")

    print(state["question"])

    return state


# ==========================================================
# Step 5 : Tool Node
# ==========================================================

def tool_node(state: State):

    print("\n========== Tool ==========")

    result = calculator.invoke(

        {

            "a":25,

            "b":75

        }

    )

    print("Calculator Result :", result)

    state["result"] = result

    return state


# ==========================================================
# Step 6 : Response Node
# ==========================================================

def response_node(state: State):

    print("\n========== Response ==========")

    print(

        f"The answer is {state['result']}"

    )

    return state


# ==========================================================
# Step 7 : Register Nodes
# ==========================================================

graph.add_node(

    "planner",

    planner_node

)

graph.add_node(

    "tool",

    tool_node

)

graph.add_node(

    "response",

    response_node

)

# ==========================================================
# Step 8 : Graph Flow
# ==========================================================

graph.set_entry_point("planner")

graph.add_edge(

    "planner",

    "tool"

)

graph.add_edge(

    "tool",

    "response"

)

graph.set_finish_point(

    "response"

)

# ==========================================================
# Step 9 : Compile
# ==========================================================

app = graph.compile()

# ==========================================================
# Step 10 : Execute
# ==========================================================

app.invoke(

    {

        "question":"What is 25 + 75?",

        "result":0

    }

)