"""
============================================================
PROJECT 07 : LANGCHAIN

Example 5 : Memory

Goal:
Understand how LangChain stores conversation history.

============================================================
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage

load_dotenv()

# ==========================================================
# Step 1 : Chat Model
# ==========================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# ==========================================================
# Step 2 : Memory
# ==========================================================

memory = InMemoryChatMessageHistory()

# ==========================================================
# Step 3 : Conversation Loop
# ==========================================================

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    # Store User Message
    memory.add_user_message(question)

    # Send Entire Conversation
    response = llm.invoke(memory.messages)

    # Store Assistant Message
    memory.add_ai_message(response.content)

    print("\nAssistant :")
    print(response.content)

    print("\nConversation Memory:\n")

    for message in memory.messages:
        print(message)