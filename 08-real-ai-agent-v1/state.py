"""
============================================================
PROJECT 08 : REAL AI AGENT

State

============================================================
"""

from typing import TypedDict


class AgentState(TypedDict):

    question: str

    tool: str

    a: int

    b: int

    result: int

    answer: str