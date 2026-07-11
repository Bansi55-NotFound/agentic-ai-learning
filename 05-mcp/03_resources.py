"""
============================================================
PROJECT 05 : MCP

Example 3 : Resources

Goal:
Expose and read MCP Resources.

============================================================
"""

from mcp.server.fastmcp import FastMCP

# ==========================================================
# Step 1 : Create Server
# ==========================================================

mcp = FastMCP("Resource Server")

# ==========================================================
# Step 2 : Resource
# ==========================================================

@mcp.resource("company://employees")
def employees():

    return """
            Name : Bansi
            
            Role : Data Engineer
            
            Company : Boeing
            """

# ==========================================================
# Step 3 : Run
# ==========================================================

if __name__ == "__main__":
    mcp.run()