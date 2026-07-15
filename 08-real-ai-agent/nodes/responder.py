from llm import get_llm
from prompts import responder_prompt


responder = responder_prompt | get_llm()


def responder_node(state):
    response = responder.invoke(
        {
            "user_input": state["user_input"],
            "tool_output": state.get("tool_output", ""),
        }
    )

    return {
        "final_response": response.content
    }