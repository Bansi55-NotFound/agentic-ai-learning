from pydantic import BaseModel, Field


class PlannerOutput(BaseModel):
    need_tool: bool = Field(
        description="Whether a tool is required to answer the user's request."
    )

    tool: str | None = Field(
        default=None,
        description="Name of the tool to use if one is required."
    )

    tool_input: dict = Field(
        default_factory=dict,
        description="Arguments that should be passed to the selected tool."
    )

    reason: str = Field(
        description="Reasoning behind the planner's decision."
    )