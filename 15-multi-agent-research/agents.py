# ============================================================
# Project 15 - Multi-Agent Research Assistant
#
# File: agents.py
#
# Purpose:
# This file creates all the AI agents used in our workflow.
# Each agent has a single responsibility.
# ============================================================

# Load environment variables
from dotenv import load_dotenv

# Access environment variables
import os

# LangChain Prompt Template
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
# Planner Agent
# ============================================================

planner_prompt = ChatPromptTemplate.from_template(
    """
You are an expert research planner.

Your job is to create a structured research plan.

Topic:
{topic}

Return:
- Main sections
- Important subtopics
- Logical order

Do not explain the topic.
Only return the research plan.
"""
)

planner_agent = (
    planner_prompt
    | llm
    | StrOutputParser()
)


# ============================================================
# Writer Agent
# ============================================================

writer_prompt = ChatPromptTemplate.from_template(
    """
You are a professional technical writer.

Using the research plan below, write a detailed report.

Research Plan:

{plan}

Write a well-structured report with headings.
"""
)

writer_agent = (
    writer_prompt
    | llm
    | StrOutputParser()
)


# ============================================================
# Reviewer Agent
# ============================================================

reviewer_prompt = ChatPromptTemplate.from_template(
    """
You are an expert reviewer.

Review the report below.

Improve:

- Grammar
- Clarity
- Structure
- Readability

Return only the improved report.

Report:

{report}
"""
)

reviewer_agent = (
    reviewer_prompt
    | llm
    | StrOutputParser()
)