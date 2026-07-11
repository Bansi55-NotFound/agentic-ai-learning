from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Company MCP Server")


# ==========================================================
# Resource
# ==========================================================

@mcp.resource("company://employees")
def employees():

    return """
Name : Bansi
Role : Data Engineer
Company : Boeing
"""


# ==========================================================
# Tool
# ==========================================================

@mcp.tool()
def calculator(a: int, b: int):

    return a + b


# ==========================================================
# Prompt
# ==========================================================

@mcp.prompt()
def interview():

    return """
You are a Senior Data Engineer.

Help the user prepare for interviews.

Provide answers with examples.
"""


if __name__ == "__main__":
    mcp.run()      