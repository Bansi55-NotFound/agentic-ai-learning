import asyncio

from mcp import ClientSession
from mcp.client.stdio import stdio_client
from mcp.client.stdio import StdioServerParameters

server = StdioServerParameters(
    command="python",
    args=["06_complete_mcp_server.py"]
)

async def main():

    async with stdio_client(server) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            # =====================================
            # Resources
            # =====================================

            resources = await session.list_resources()

            print("\nResources")

            for resource in resources.resources:
                print(resource.uri)

            # =====================================
            # Tools
            # =====================================

            tools = await session.list_tools()

            print("\nTools")

            for tool in tools.tools:
                print(tool.name)

            # =====================================
            # Prompts
            # =====================================

            prompts = await session.list_prompts()

            print("\nPrompts")

            for prompt in prompts.prompts:
                print(prompt.name)

            # =====================================
            # Read Resource
            # =====================================

            resource = await session.read_resource(
                "company://employees"
            )

            print("\nEmployee Resource\n")
            print(resource)

            # =====================================
            # Call Tool
            # =====================================

            result = await session.call_tool(
                "calculator",
                {
                    "a": 25,
                    "b": 75
                }
            )

            print("\nCalculator Result\n")
            print(result)

            # =====================================
            # Get Prompt
            # =====================================

            prompt = await session.get_prompt(
                "interview"
            )

            print("\nInterview Prompt\n")
            print(prompt)

if __name__ == "__main__":

    asyncio.run(main())