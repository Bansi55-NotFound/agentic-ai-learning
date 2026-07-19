from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Answer in bullet points.",
        "Be concise."
    ]
)

agent.print_response(
    "Explain the new features of Python 3.13."
)