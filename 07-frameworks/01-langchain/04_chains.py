from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# ==================================================
# Step 1 : Chat Model
# ==================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# ==================================================
# Step 2 : Prompt
# ==================================================

prompt = PromptTemplate.from_template(
    """
You are an AI Assistant.

Answer the following question.

Question:
{question}
"""
)

# ==================================================
# Step 3 : Parser
# ==================================================

parser = StrOutputParser()

# ==================================================
# Step 4 : Create Chain
# ==================================================

chain = prompt | llm | parser

# ==================================================
# Step 5 : Invoke
# ==================================================

response = chain.invoke(
    {
        "question": "What is LangChain?"
    }
)

print(response)