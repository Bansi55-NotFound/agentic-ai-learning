from crewai.tools import BaseTool


class CalculatorTool(BaseTool):
    name: str = "Calculator"
    description: str = "Perform mathematical calculations."

    def _run(
        self,
        left_value: str,
        op_symbol: str,
        right_value: str,
    ) -> str:

        left = float(left_value)
        right = float(right_value)

        if op_symbol == "+":
            return str(left + right)

        if op_symbol == "-":
            return str(left - right)

        if op_symbol == "*":
            return str(left * right)

        if op_symbol == "/":
            return str(left / right)

        return "Unsupported operator"