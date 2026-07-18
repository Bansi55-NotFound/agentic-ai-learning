from dotenv import load_dotenv
import os

from smolagents import (
    CodeAgent,
    InferenceClientModel,
    DuckDuckGoSearchTool,
)

load_dotenv()

# Load Hugging Face Model
model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    token=os.getenv("HF_TOKEN"),
)

# Create Agent
agent = CodeAgent(
    model=model,
    tools=[DuckDuckGoSearchTool()],
)

question = """
Research the latest version of Python.

Tell me:
1. Current stable version
2. Three major new features
3. Why developers should upgrade
4. Give the answer in bullet points.
"""

response = agent.run(question)

print("\n========== FINAL REPORT ==========\n")
print(response)