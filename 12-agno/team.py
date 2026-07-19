from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq

load_dotenv()

researcher = Agent(
    name="Researcher",
    model=Groq(id="llama-3.3-70b-versatile"),
    role="Research topics",
)

writer = Agent(
    name="Writer",
    model=Groq(id="llama-3.3-70b-versatile"),
    role="Write well-structured content",
)

print(researcher)
print(writer)