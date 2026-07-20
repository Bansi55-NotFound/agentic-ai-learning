# ============================================================
# Project 16 - AI Document Intelligence
#
# File: analyzer.py
#
# Purpose:
# Analyze the extracted document using an LLM.
# ============================================================

# Load environment variables
from dotenv import load_dotenv

# Access environment variables
import os

# Prompt Template
from langchain_core.prompts import ChatPromptTemplate

# Output Parser
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
You are an intelligent document analysis assistant.

Analyze the document below.

Document:

{document}

Return the following:

1. Document Type

2. Summary

3. Important Information

4. Key Skills (if applicable)

5. Experience (if applicable)

6. Education (if applicable)

7. Important Dates

8. Overall Insights

Return the response in clean markdown.
"""
)


# ============================================================
# Build Chain
# ============================================================

analysis_chain = (
    prompt
    | llm
    | StrOutputParser()
)


# ============================================================
# Analyze Document
# ============================================================

def analyze_document(document: str) -> str:
    """
    Analyze the extracted document.

    Args:
        document: Extracted document text.

    Returns:
        AI-generated analysis.
    """

    return analysis_chain.invoke(
        {
            "document": document
        }
    )