"""
============================================================
PROJECT 08 : REAL AI AGENT

Prompts

============================================================
"""

PLANNER_PROMPT = """
You are a planning agent.

The user question is:

{question}

If calculation is required,
extract the numbers.

Return:

Tool
First Number
Second Number
"""

RESPONSE_PROMPT = """
User Question:

{question}

Calculator Result:

{result}

Generate a natural language answer.
"""