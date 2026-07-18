from smolagents import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Args:
        expression: Mathematical expression to evaluate.
    """
    return str(eval(expression))