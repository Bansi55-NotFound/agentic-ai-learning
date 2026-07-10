"""
============================================================
PROJECT 04 : AI AGENT
Example 1 : Basic Agent Setup
============================================================

Goal:
Build our own AI Agent from scratch.

Today:
✓ Connect Gemini
✓ Take User Goal
✓ Get AI Response

Later:
Planning
Memory
Tool Calling
Reflection

============================================================
"""

from google import genai
from dotenv import load_dotenv
import os
import time

# ==========================================================
# Step 1 : Load Environment Variables
# ==========================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# ==========================================================
# Step 2 : Create Gemini Client
# ==========================================================

client = genai.Client(api_key=api_key)

# ==========================================================
# Step 3 : Get User Goal
# ==========================================================

goal = input("Enter your goal: ")

# ==========================================================
# Step 4 : Generate Response
# ==========================================================

planning_prompt = f"""
You are an AI Planning Agent.

You are an AI Planning Agent.

Break the goal into only the tasks that an AI assistant can perform.

Do not include tasks that require physical actions by the user.

Return only numbered steps.

Goal:
{goal}

Return ONLY the numbered steps.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=planning_prompt
)

plan = response.text

print("\nExecution Plan:\n")
print(plan)
# ==========================================================
# Step 5 : Parse Plan
# ==========================================================

steps = plan.split("\n")

steps = [step.strip() for step in steps if step.strip()]

print("\nParsed Steps:\n")

for step in steps:
    print(step)

# ==========================================================
# Step 6 : Execute One Step
# ==========================================================

def execute_step(step):

    print(f"\nExecuting: {step}")

    max_retries = 3

    for attempt in range(max_retries):

        try:

            execution_prompt = f"""
            You are an AI Execution Agent.

            Goal:
            {goal}

            Current Step:
            {step}

            Rules:
            - Execute ONLY the current step.
            - Keep the response under 5 bullet points.
            - Do not explain in detail.
            - Do not generate a final answer.
            - This output will be used by another AI step.
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=execution_prompt
            )

            return response.text

        except Exception as e:

            print(f"Attempt {attempt + 1} failed: {e}")

            if attempt < max_retries - 1:
                print("Retrying in 5 seconds...\n")
                time.sleep(5)

    return "Execution Failed"
# ==========================================================
# Step 7 : Execute Plan
# ==========================================================

results = []

for step in steps:

    output = execute_step(step)

    results.append(output)

    print("\nResult:\n")
    print(output)