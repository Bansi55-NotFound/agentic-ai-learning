from llm import get_llm
from prompts import planner_prompt
from schemas.planner_output import PlannerOutput


planner = planner_prompt | get_llm().with_structured_output(PlannerOutput)


def planner_node(state):
    result = planner.invoke(
        {
            "user_input": state["user_input"]
        }
    )

    return {
        "planner_output": result
    }