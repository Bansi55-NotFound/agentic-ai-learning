from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    add_history_to_messages=True,
)

agent.print_response("My name is Bansi.")
agent.print_response("What is my name?")