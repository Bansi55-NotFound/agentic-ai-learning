# ============================================================
# Project 17 - AI Data Engineering Assistant
#
# File: assistant.py
#
# Purpose:
# AI Backend with Conversation Memory
# ============================================================

import os

from dotenv import load_dotenv

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq

from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),

        # Conversation History
        MessagesPlaceholder(variable_name="history"),

        # Current User Question
        ("human", "{question}")
    ]
)

# Build Chain
assistant_chain = (
    prompt
    | llm
    | StrOutputParser()
)

# Ask Assistant
def ask_assistant(question: str, history: list) -> str:
    """
    Ask the AI assistant.

    Args:
        question: Current user question.
        history: Previous conversation.

    Returns:
        AI response.
    """

    return assistant_chain.invoke(
        {
            "question": question,
            "history": history
        }
    )