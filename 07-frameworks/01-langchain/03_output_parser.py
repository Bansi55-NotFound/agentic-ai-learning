from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# ==========================================
# Step 1 : Chat Model
# ==========================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# ==========================================
# Step 2 : Output Parser
# ==========================================

parser = StrOutputParser()

# ==========================================
# Step 3 : LLM
# ==========================================

response = llm.invoke(
    "Who invented Python?"
)
# print(response)

# ==========================================
# Step 4 : Parse
# ==========================================

output = parser.invoke(response)

print(output)