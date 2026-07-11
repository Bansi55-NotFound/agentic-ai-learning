"""
============================================================
PROJECT 05 : MCP

Example 2 : Basic MCP Client

Goal:
Connect to an MCP Server and discover available tools.

============================================================
"""

import asyncio

from mcp import ClientSession
from mcp.client.stdio import stdio_client
from mcp.client.stdio import StdioServerParameters

# ==========================================================
# Step 1 : Server Details
# ==========================================================

server_params = StdioServerParameters(
    command="python",
    args=["01_basic_mcp_server.py"]
)

# ==========================================================
# Step 2 : Main Function
# ==========================================================

async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("\nConnected to MCP Server.\n")

            # Discover Tools
            tools = await session.list_tools()

            print("Available Tools:\n")

            for tool in tools.tools:
                print(tool.name)

            # ==================================================
            # Call Tool
            # ==================================================

            result = await session.call_tool(
                "calculator",
                {
                    "a": 25,
                    "b": 75
                }
            )

            print("\nTool Result:\n")
            print(result)
# ==========================================================
# Step 3 : Run Client
# ==========================================================

if __name__ == "__main__":
    asyncio.run(main())