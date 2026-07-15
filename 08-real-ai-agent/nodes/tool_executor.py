from tools.registry import TOOLS


def tool_executor_node(state):
    planner_output = state["planner_output"]

    tool_name = planner_output.tool
    tool_input = planner_output.tool_input

    tool = TOOLS.get(tool_name)

    if tool is None:
        return {
            "tool_output": f"Unknown tool: {tool_name}"
        }

    result = tool(**tool_input)

    return {
        "tool_output": result
    }