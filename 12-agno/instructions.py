from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Always answer in bullet points.",
        "Keep responses concise.",
        "Explain like you're teaching a beginner."
    ],
)

agent.print_response(
    "Explain Retrieval Augmented Generation."
)