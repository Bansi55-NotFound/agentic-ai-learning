from dotenv import load_dotenv
import os

from smolagents import (
    CodeAgent,
    InferenceClientModel,
    DuckDuckGoSearchTool,
)

load_dotenv()

model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    token=os.getenv("HF_TOKEN"),
)

agent = CodeAgent(
    model=model,
    tools=[DuckDuckGoSearchTool()],
)

response = agent.run(
    "Find the population of Japan and India, then tell me which country has the larger population and by approximately how much."
)

print("\nFinal Answer:\n")
print(response)