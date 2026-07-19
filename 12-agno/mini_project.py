from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Answer in bullet points.",
        "Keep answers concise.",
        "Act as a senior AI mentor."
    ]
)

agent.print_response(
    """
    Compare LangChain, LangGraph, CrewAI,
    SmolAgents and Agno.

    Mention:
    - Use cases
    - Advantages
    - Limitations
    """
)