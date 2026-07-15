import os

from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# LLM Configuration
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0
MAX_TOKENS = 1024