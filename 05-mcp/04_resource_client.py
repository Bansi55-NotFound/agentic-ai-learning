import asyncio

from mcp import ClientSession
from mcp.client.stdio import stdio_client
from mcp.client.stdio import StdioServerParameters

server = StdioServerParameters(
    command="python",
    args=["03_resources.py"]
)

async def main():

    async with stdio_client(server) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("Connected!\n")

            # ===========================
            # List Resources
            # ===========================

            resources = await session.list_resources()

            print("Resources:\n")

            for resource in resources.resources:

                print(resource.uri)

            # ===========================
            # Read Resource
            # ===========================

            result = await session.read_resource(
                "company://employees"
            )

            print("\nResource Content:\n")

            print(result)

if __name__ == "__main__":

    asyncio.run(main())