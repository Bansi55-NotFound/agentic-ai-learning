"""
============================================================
PROJECT 05 : MCP

Example 5 : Prompts

Goal:
Expose reusable prompts through MCP.

============================================================
"""

from mcp.server.fastmcp import FastMCP

# ==========================================================
# Step 1 : Create MCP Server
# ==========================================================

mcp = FastMCP("Prompt Server")

# ==========================================================
# Step 2 : Prompt
# ==========================================================

@mcp.prompt()
def code_review(language: str):

    return f"""
You are a senior {language} developer.

Review the given code.

Check for:

1. Bugs
2. Performance
3. Security
4. Best Practices

Provide detailed suggestions.
"""

# ==========================================================
# Step 3 : Run
# ==========================================================

if __name__ == "__main__":
    mcp.run()