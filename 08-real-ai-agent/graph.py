from langgraph.graph import StateGraph, START, END

from state import AgentState
from nodes.planner import planner_node
from nodes.tool_executor import tool_executor_node
from nodes.responder import responder_node


def should_use_tool(state: AgentState):
    if state["planner_output"].need_tool:
        return "tool"

    return "response"


graph_builder = StateGraph(AgentState)

graph_builder.add_node("planner", planner_node)
graph_builder.add_node("tool_executor", tool_executor_node)
graph_builder.add_node("responder", responder_node)

graph_builder.add_edge(START, "planner")

graph_builder.add_conditional_edges(
    "planner",
    should_use_tool,
    {
        "tool": "tool_executor",
        "response": "responder",
    },
)

graph_builder.add_edge("tool_executor", "responder")

graph_builder.add_edge("responder", END)

graph = graph_builder.compile()