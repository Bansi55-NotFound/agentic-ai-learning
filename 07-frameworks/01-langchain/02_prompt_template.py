from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

# ===========================================
# Create LLM
# ===========================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# ===========================================
# Create Prompt Template
# ===========================================

template = PromptTemplate.from_template(
    """
You are a helpful AI Assistant.

Question:
{question}
"""
)

# ===========================================
# Fill Template
# ===========================================

prompt = template.invoke(
    {
        "question": "Explain RAG in simple words."
    }
)

# ===========================================
# Send to LLM
# ===========================================

response = llm.invoke(prompt)

print(response.content)