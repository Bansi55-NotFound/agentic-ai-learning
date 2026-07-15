from typing import Union

Number = Union[int, float]


def calculator(num1: Number, num2: Number, operation: str):
    operation = operation.lower().strip()

    operations = {
        "add": lambda a, b: a + b,
        "addition": lambda a, b: a + b,
        "+": lambda a, b: a + b,

        "subtract": lambda a, b: a - b,
        "subtraction": lambda a, b: a - b,
        "-": lambda a, b: a - b,

        "multiply": lambda a, b: a * b,
        "multiplication": lambda a, b: a * b,
        "*": lambda a, b: a * b,

        "divide": lambda a, b: a / b,
        "division": lambda a, b: a / b,
        "/": lambda a, b: a / b,
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    return operations[operation](num1, num2)