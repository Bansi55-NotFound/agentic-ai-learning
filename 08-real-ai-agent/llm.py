from langchain_groq import ChatGroq

from config import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
)

def get_llm():
    return ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
