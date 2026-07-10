"""
============================================================
PROJECT 07 : AI AGENT WITH TOOLS

Goal:
Build an AI Agent that can:

✓ Plan
✓ Decide whether a tool is needed
✓ Execute Python tools
✓ Use Working Memory
✓ Reflection
                 User Goal
                     │
                     ▼
                 Planning
                     │
                     ▼
               Parse Plan
                     │
                     ▼
            Execute Every Step
                     │
                     ▼
         Decide Whether Tool Needed
             │                 │
             ▼                 ▼
      Execute Tool       Ask LLM Directly
             │                 │
             └──────────┬──────┘
                        ▼
                Store Result
                        ▼
               Working Memory
                        ▼
                 Reflection
                        ▼
                 Final Answer
============================================================
"""

from groq import Groq
from dotenv import load_dotenv
import os
import json

# ==========================================================
# Step 1 : Load Environment Variables
# ==========================================================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==========================================================
# Step 2 : Python Tools
# ==========================================================

def calculator(a, b):
    return a + b


def get_weather(city):
    return f"The weather in {city} is 29°C and Sunny."


def search_places(city):
    return [
        "Baga Beach",
        "Calangute Beach",
        "Fort Aguada"
    ]


# ==========================================================
# Step 3 : Python Tool Registry
# ==========================================================

tool_map = {
    "calculator": calculator,
    "get_weather": get_weather,
    "search_places": search_places
}

# ==========================================================
# Step 4 : Memory
# ==========================================================

conversation = []

# ==========================================================
# Step 5 : User Goal
# ==========================================================

goal = input("Enter your goal: ")

conversation.append(
    {
        "role": "user",
        "content": goal
    }
)

# ==========================================================
# Step 6 : Planning
# ==========================================================

planning_prompt = f"""
You are an AI Planning Agent.

Create ONLY meaningful steps.

Avoid unnecessary decomposition.

If the task is simple,
return only one step.

Goal:

{goal}
"""

planning_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": planning_prompt
        }
    ]
)

plan = planning_response.choices[0].message.content

print("\nExecution Plan\n")
print(plan)

# ==========================================================
# Step 7 : Parse Plan
# ==========================================================

steps = [
    step.strip()
    for step in plan.split("\n")
    if step.strip()
]

# ==========================================================
# Step 8 : Tool Decision Function
# ==========================================================

def decide_tool(step):

    tool_prompt = f"""
You are an AI Agent.

Available tools:

1. calculator(a,b)

2. get_weather(city)

3. search_places(city)

Current Step:

{step}

Rules:

If a tool is needed return JSON.

Example:

{{
    "tool":"calculator",
    "arguments":{{
        "a":20,
        "b":30
    }}
}}

If no tool is needed

{{
    "tool":"none",
    "arguments":{{}}
}}

Return ONLY JSON.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": tool_prompt
            }
        ],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)

# ==========================================================
# Step 9 : Execute Step
# ==========================================================

def execute_step(step, previous_results):

    tool_request = decide_tool(step)

    tool = tool_request["tool"]

    if tool != "none":

        print(f"\nTool Selected : {tool}")

        args = tool_request["arguments"]

        result = tool_map[tool](**args)

        return str(result)

    execution_prompt = f"""
        Previous Results:
        
        {previous_results}
        
        Current Step:
        
        {step}
        
        Complete only this step.
        """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":execution_prompt
            }
        ]
    )

    return response.choices[0].message.content

# ==========================================================
# Step 10 : Execute Complete Plan
# ==========================================================

results = []
previous_results = ""

for step in steps:

    print("\n" + "=" * 60)
    print(f"Executing : {step}")
    print("=" * 60)

    output = execute_step(step, previous_results)

    print("\nResult:\n")
    print(output)

    results.append(output)

    previous_results += f"""

Step:
{step}

Result:
{output}
"""

# ==========================================================
# Step 11 : Combine Results
# ==========================================================

combined_results = "\n\n".join(results)

print("\n" + "=" * 60)
print("COMBINED RESULTS")
print("=" * 60)

print(combined_results)

# ==========================================================
# Step 12 : Reflection Prompt
# ==========================================================

reflection_prompt = f"""
You are a senior AI reviewer.

Original Goal:

{goal}

The AI Agent executed the following steps:

{combined_results}

Your task:

- Produce one final answer.
- Remove duplicate information.
- Improve clarity.
- Improve grammar.
- Improve formatting.
- Return ONLY the final answer.
"""

# ==========================================================
# Step 13 : Reflection
# ==========================================================

reflection_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": reflection_prompt
        }
    ]
)

final_answer = reflection_response.choices[0].message.content

# ==========================================================
# Step 14 : Store in Memory
# ==========================================================

conversation.append(
    {
        "role": "assistant",
        "content": final_answer
    }
)

# ==========================================================
# Step 15 : Final Answer
# ==========================================================

print("\n")
print("=" * 70)
print("FINAL ANSWER")
print("=" * 70)
print(final_answer)
print("=" * 70)