"""
============================================================
PROJECT 08 : LANGGRAPH

Example 7 : Memory

============================================================
"""

from typing import TypedDict
from langgraph.graph import StateGraph

# ==========================================================
# Step 1 : State
# ==========================================================

class State(TypedDict):

    history: list

# ==========================================================
# Step 2 : Graph
# ==========================================================

graph = StateGraph(State)

# ==========================================================
# Step 3 : Chat Node
# ==========================================================

def chat_node(state: State):

    print("\nConversation History")

    for message in state["history"]:

        print(message)

    state["history"].append("AI : Nice to meet you!")

    return state

# ==========================================================
# Step 4 : Register Node
# ==========================================================

graph.add_node(
    "chat",
    chat_node
)

graph.set_entry_point("chat")
graph.set_finish_point("chat")

# ==========================================================
# Step 5 : Compile
# ==========================================================

app = graph.compile()

# ==========================================================
# Step 6 : Run
# ==========================================================

app.invoke(
    {

        "history":[

            "Human : Hi",

            "Human : My name is Bansi"

        ]

    }
)