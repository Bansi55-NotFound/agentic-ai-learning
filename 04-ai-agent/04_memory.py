"""
============================================================
PROJECT 04 : AI AGENT
Example 4 : Memory
============================================================

Goal:
Understand how AI Agents remember previous conversations.

Workflow:

User
    ↓
Store Memory
    ↓
Conversation History
    ↓
LLM
    ↓
Response

============================================================
"""

from groq import Groq
from dotenv import load_dotenv
import os

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
# Step 3 : Memory
# ==========================================================

conversation = []

[
    {
        "role":"user",
        "content":"Hi"
    },

    {
        "role":"assistant",
        "content":"Hello"
    },

    {
        "role":"user",
        "content":"My name is Bansi"
    }
]

while True:

    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        break

    conversation.append(
            {
                "role": "user",
                "content": user_input
            }
        )
    # ==========================================================
    # Step 5 : Send Conversation to LLM
    # ==========================================================

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation[-10:]
    )

    # ==========================================================
    # Step 6 : Get Assistant Response
    # ==========================================================

    assistant_response = response.choices[0].message.content

    print("\nAssistant :")
    print(assistant_response)

    # ==========================================================
    # Step 7 : Store Assistant Response
    # ==========================================================

    conversation.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )

    # ==========================================================
    # Step 8 : Print Memory
    # ==========================================================

    print("\nConversation Memory:\n")

    for message in conversation:
        print(message)