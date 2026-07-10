"""
============================================================
PROJECT 04 : AI AGENT
Example 5 : Reflection
============================================================

Goal:
Understand how AI Agents improve their own answers.

Workflow:

User
    ↓
Generate Draft
    ↓
Review Draft
    ↓
Improve Draft
    ↓
Final Answer

============================================================
"""

from groq import Groq
from dotenv import load_dotenv
import os

# ==========================================================
# Step 1 : Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Step 2 : Create Groq Client
# ==========================================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==========================================================
# Step 3 : Get User Request
# ==========================================================

user_request = input("Enter your request: ")

# ==========================================================
# Step 4 : Generate Draft
# ==========================================================

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": user_request
        }
    ]
)

draft = response.choices[0].message.content

print("\nDraft Response:\n")
print(draft)

# ==========================================================
# Step 5 : Reflection Prompt
# ==========================================================

reflection_prompt = f"""
You are a senior reviewer.

Review the following response.

Check for:
- Accuracy
- Clarity
- Completeness
- Grammar
- Professionalism

If it can be improved,
rewrite it.

If it is already good,
return it as is.

Response:

{draft}
"""

# ==========================================================
# Step 6 : Reflect
# ==========================================================

reflection_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": reflection_prompt
        }
    ]
)

# ==========================================================
# Step 7 : Improved Response
# ==========================================================

improved_response = reflection_response.choices[0].message.content

print("\nImproved Response:\n")
print(improved_response)