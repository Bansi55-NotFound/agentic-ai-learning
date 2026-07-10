"""
============================================================
PROJECT 04 : AI AGENT
Example 3 : Native Function Calling
============================================================

Goal:
Understand Native Function Calling using Groq.

Workflow:

User Request
      ↓
LLM selects a function
      ↓
SDK returns Tool Call
      ↓
Python executes function
      ↓
LLM generates final response

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
# Step 3 : LLM Tool Registry
# ==========================================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Add two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["a", "b"]
            }
        }
    }
]

# ==========================================================
# Step 4 : Python Tool Registry
# ==========================================================

tool_map = {
    "calculator": calculator,
    "get_weather": get_weather,
    "search_places": search_places
}

# ==========================================================
# Step 5 : Get User Request
# ==========================================================

user_request = input("Enter your request: ")

# ==========================================================
# Step 6 : Ask LLM
# ==========================================================

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": user_request
        }
    ],
    tools=tools,
    tool_choice="auto"
)

# ==========================================================
# Step 7 : Get Assistant Message
# ==========================================================

message = response.choices[0].message

print("\nAssistant Message:\n")
print(message)

# ==========================================================
# Step 8 : Check Whether Tool Call Exists
# ==========================================================

if message.tool_calls:

    print("\nLLM requested a tool.")

    # ======================================================
    # Step 9 : Get Tool Call
    # ======================================================

    tool_call = message.tool_calls[0]

    print("\nTool Call:\n")
    print(tool_call)

    # ======================================================
    # Step 10 : Extract Function Name
    # ======================================================

    tool_name = tool_call.function.name

    print("\nFunction Name:")
    print(tool_name)

    # ======================================================
    # Step 11 : Extract Arguments
    # ======================================================

    print("\nArguments Before Parsing:")
    print(tool_call.function.arguments)
    print(type(tool_call.function.arguments))

    arguments = json.loads(tool_call.function.arguments)

    print("\nArguments After Parsing:")
    print(arguments)
    print(type(arguments))

    # ======================================================
    # Step 12 : Execute Tool
    # ======================================================

    result = tool_map[tool_name](**arguments)

    print("\nTool Result:")
    print(result)

    # ======================================================
    # Step 13 : Generate Final Response
    # ======================================================

    final_prompt = f"""
User Request:
{user_request}

Tool Used:
{tool_name}

Tool Result:
{result}

Generate a helpful response for the user.
Do not mention tools or function calling.
"""

    final_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    print("\nFinal Answer:\n")
    print(final_response.choices[0].message.content)

else:

    print("\nNo Tool Required.")

    print("\nAssistant Response:\n")
    print(message.content)