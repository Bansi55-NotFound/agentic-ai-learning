# ============================================================
# Project 16 - AI Document Intelligence
#
# File: qa.py
#
# Purpose:
# Answer user questions using the uploaded document.
# ============================================================

# Load environment variables
from dotenv import load_dotenv

# Access environment variables
import os

# Prompt template
from langchain_core.prompts import ChatPromptTemplate

# Output parser
from langchain_core.output_parsers import StrOutputParser

# Groq LLM
from langchain_groq import ChatGroq


# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()


# ============================================================
# Initialize LLM
# ============================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


# ============================================================
# Prompt
# ============================================================

prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Answer ONLY using the information contained in the document.

If the answer cannot be found in the document, reply:

"I couldn't find that information in the uploaded document."

Document:
{document}

Question:
{question}
"""
)


# ============================================================
# Chain
# ============================================================

qa_chain = (
    prompt
    | llm
    | StrOutputParser()
)


# ============================================================
# Function
# ============================================================

def answer_question(document: str, question: str) -> str:
    """
    Answer questions about the uploaded document.

    Args:
        document: Extracted document text.
        question: User's question.

    Returns:
        AI answer.
    """

    return qa_chain.invoke(
        {
            "document": document,
            "question": question
        }
    )