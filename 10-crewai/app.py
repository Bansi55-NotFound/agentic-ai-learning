from crewai import Agent, Task, Crew, LLM, Process
from calculator_tool import CalculatorTool

calculator = CalculatorTool()

llm = LLM(
    model="ollama/qwen2.5:1.5b",
    base_url="http://localhost:11434",
)

travel_agent = Agent(
    role="Travel Expert",
    goal="Help users with travel planning and calculations",
    backstory="You are an expert travel planner.",
    llm=llm,
    tools=[calculator],
    verbose=True,
)

travel_task = Task(
    description="Calculate 125 * 48",
    expected_output="The correct multiplication result.",
    agent=travel_agent,
)

writer_agent = Agent(
    role="Travel Writer",
    goal="Write engaging travel itineraries.",
    backstory="You are an expert travel writer.",
    llm=llm,
    verbose=True,
)

writer_task = Task(
    description="""
    Write a beautiful travel itinerary
    using the researched information.
    """,
    expected_output="A well-formatted travel itinerary.",
    agent=writer_agent,
)

travel_crew = Crew(
    agents=[travel_agent, writer_agent],
    tasks=[travel_task, writer_task],
    memory=True,
    process=Process.sequential,
    verbose=True,
)
result = travel_crew.kickoff()

print(result)