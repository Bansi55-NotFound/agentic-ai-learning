"""
============================================================
PROJECT 04 : AI AGENT
Example 2 : Tool Calling
============================================================

Goal:
Understand how Tool Calling works internally.

Workflow:

User Request
      ↓
LLM selects a tool
      ↓
LLM returns JSON
      ↓
Python parses JSON
      ↓
Python executes the tool
      ↓
Display Result

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

# ==========================================================
# Step 2 : Create Groq Client
# ==========================================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==========================================================
# Tool 1 : Calculator
# ==========================================================

def calculator(a, b):
    return a + b


# ==========================================================
# Tool 2 : Weather
# ==========================================================

def get_weather(city):
    return f"The weather in {city} is 29°C and Sunny."


# ==========================================================
# Tool 3 : Tourist Places
# ==========================================================

def search_places(city):
    return [
        "Baga Beach",
        "Calangute Beach",
        "Fort Aguada"
    ]


# ==========================================================
# Step 3 : Get User Request
# ==========================================================

user_request = input("Enter your request: ")

# ==========================================================
# Step 4 : Ask LLM to Select a Tool
# ==========================================================

tool_prompt = f"""
You are an AI Agent.

Available Tools:

1. calculator(a, b)
   Purpose: Add two numbers.

2. get_weather(city)
   Purpose: Get weather of a city.

3. search_places(city)
   Purpose: Get famous tourist places.

User Request:
{user_request}

Rules:
- Select ONLY ONE tool.
- Select a tool ONLY if it can completely satisfy the user's request.
- If no suitable tool exists, return:

{{
    "tool": "none",
    "arguments": {{}},
    "reason": "No suitable tool available."
}}

- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT use ```json.
- Do NOT add any explanation.

Examples:

User:
Add 22 and 88

Output:
{{
    "tool": "calculator",
    "arguments": {{
        "a": 22,
        "b": 88
    }}
}}

User:
What's the weather in Goa?

Output:
{{
    "tool": "get_weather",
    "arguments": {{
        "city": "Goa"
    }}
}}

User:
Show tourist places in Goa

Output:
{{
    "tool": "search_places",
    "arguments": {{
        "city": "Goa"
    }}
}}

User:
How far is Pune from Mumbai?

Output:
{{
    "tool": "none",
    "arguments": {{}},
    "reason": "No suitable tool available."
}}
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

llm_response = response.choices[0].message.content

print("\nLLM Response:\n")
print(llm_response)

# ==========================================================
# Step 5 : Convert JSON to Python Dictionary
# ==========================================================

tool_request = json.loads(llm_response)

print("\nPython Dictionary:\n")
print(tool_request)

# ==========================================================
# Step 6 : Tool Registry
# ==========================================================

tool_map = {
    "calculator": calculator,
    "get_weather": get_weather,
    "search_places": search_places
}

# ==========================================================
# Step 7 : Execute Selected Tool
# ==========================================================

tool_name = tool_request["tool"]

arguments = tool_request["arguments"]


if tool_name == "none":

    print("\nNo suitable tool available.")
    print(tool_request["reason"])

elif tool_name in tool_map:

    arguments = tool_request["arguments"]

    result = tool_map[tool_name](**arguments)

    print("\nTool Result:\n")
    print(result)
    # ==========================================================
    # Step 8 : Generate Final Response
    # ==========================================================

    final_prompt = f"""
    You are an AI Assistant.

    User Request:
    {user_request}

    Tool Used:
    {tool_name}

    Tool Result:
    {result}

    Generate a natural, helpful response for the user.
    Do not mention tools or JSON.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ],
        temperature=0
    )

    print("\nFinal Answer:\n")
    print(response.choices[0].message.content)

else:

    print("\nInvalid tool returned by LLM.")

