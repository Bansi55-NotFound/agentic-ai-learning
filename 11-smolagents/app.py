from dotenv import load_dotenv
import os

from smolagents import CodeAgent, InferenceClientModel

from calculator_tool import calculator

load_dotenv()

model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    token=os.getenv("HF_TOKEN")
)

agent = CodeAgent(
    model=model,
    tools=[calculator]
)

response = agent.run(
    "What is 458 * 234?"
)

print(response)