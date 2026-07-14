"""
============================================================
PROJECT 08 : REAL AI AGENT

Tools

============================================================
"""

from langchain_core.tools import tool


@tool
def calculator(a: int, b: int) -> int:
    """
    Add two integers.
    """

    return a + b