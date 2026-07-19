# ============================================================
# Project 14 - AI SQL Assistant
#
# File: sql_agent.py
#
# Purpose:
# Connect an LLM with a SQL database so it can answer
# natural language questions using SQL.
# ============================================================

# Load environment variables from .env
from dotenv import load_dotenv

# Used to access environment variables
import os

# LangChain SQL Database wrapper
from langchain_community.utilities import SQLDatabase

# Groq LLM
from langchain_groq import ChatGroq

# SQL Agent creator
from langchain_community.agent_toolkits import create_sql_agent


# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()


# ============================================================
# Connect to SQLite Database
# ============================================================

# SQLite database URI
db = SQLDatabase.from_uri("sqlite:///employees.db")

# ============================================================
# Explore the Database
# ============================================================

print("Tables:")
print(db.get_usable_table_names())

print("\nDatabase Schema:")
print(db.get_table_info())

# ============================================================
# Initialize LLM
# ============================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


# ============================================================
# Create SQL Agent
# ============================================================

agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)


# ============================================================
# Ask Questions
# ============================================================
# ============================================================
# Function to Ask SQL Questions
# ============================================================

def ask_database(question: str) -> str:
    """
    Sends a natural language question to the SQL Agent
    and returns the answer.
    """

    response = agent.invoke(question)

    return response["output"]


# ============================================================
# Terminal Testing
# ============================================================

if __name__ == "__main__":

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        print("\n🤖 Answer:\n")

        print(ask_database(question))