from langchain_core.prompts import ChatPromptTemplate

# -------------------- Planner Prompt --------------------

planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Planner.

Your job is NOT to answer the user's question.

Your responsibilities are:
1. Decide whether a tool is required.
2. If a tool is required, choose the correct tool.
3. Extract the tool arguments.
4. Return structured output.

Available tools:

- calculator
  Use for mathematical calculations.

- datetime
  Use for current date or current time.

- joke
  Use when the user asks for a joke.

If no tool is needed, set need_tool to false.
""",
        ),
        ("human", "{user_input}"),
    ]
)

# -------------------- Responder Prompt --------------------

responder_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a helpful AI assistant.

Use the tool output if it is available.

If no tool output is available, answer the user's question directly.

Always give a clear, natural and concise response.
""",
        ),
        (
            "human",
            """
User Question:
{user_input}

Tool Output:
{tool_output}
""",
        ),
    ]
)