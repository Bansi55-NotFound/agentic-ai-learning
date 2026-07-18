from dotenv import load_dotenv
import os

from smolagents import (
    CodeAgent,
    InferenceClientModel,
    DuckDuckGoSearchTool,
)

load_dotenv()

# Load Hugging Face model
model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    token=os.getenv("HF_TOKEN"),
)

# Built-in web search tool
search_tool = DuckDuckGoSearchTool()

# Create Agent
agent = CodeAgent(
    model=model,
    tools=[search_tool],
)

# Ask a question
response = agent.run(
    "What are the latest AI news today?"
)

print("\nFinal Answer:\n")
print(response)