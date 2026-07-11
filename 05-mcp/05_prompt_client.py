import asyncio

from mcp import ClientSession
from mcp.client.stdio import stdio_client
from mcp.client.stdio import StdioServerParameters

server = StdioServerParameters(
    command="python",
    args=["05_prompts.py"]
)

async def main():

    async with stdio_client(server) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("Connected!\n")

            # =====================================
            # List Prompts
            # =====================================

            prompts = await session.list_prompts()

            print("Available Prompts:\n")

            for prompt in prompts.prompts:
                print(prompt.name)

            # =====================================
            # Get Prompt
            # =====================================

            prompt = await session.get_prompt(
                "code_review",
                {
                    "language": "Python"
                }
            )

            print("\nPrompt:\n")

            print(prompt)

if __name__ == "__main__":

    asyncio.run(main())