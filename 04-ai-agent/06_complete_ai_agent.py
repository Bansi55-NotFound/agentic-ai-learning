"""
============================================================
PROJECT 04 : AI AGENT
Example 6 : Complete AI Agent
============================================================

Goal:
Combine everything learned into one AI Agent.

Workflow:

User
    ↓
Planning
    ↓
Execute Steps
    ↓
Reflection
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
# Step 3 : Memory
# ==========================================================

conversation = []

# ==========================================================
# Step 4 : Get User Goal
# ==========================================================

goal = input("Enter your goal: ")

conversation.append(
    {
        "role": "user",
        "content": goal
    }
)

# ==========================================================
# Step 5 : Planning
# ==========================================================

planning_prompt = f"""
You are an AI Planning Agent.

Break the following goal into small actionable steps.

Return ONLY numbered steps.

Goal:
{goal}
"""

planning_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": planning_prompt
        }
    ]
)

plan = planning_response.choices[0].message.content

print("\nExecution Plan:\n")
print(plan)

# ==========================================================
# Step 6 : Parse Plan
# ==========================================================

steps = plan.split("\n")
steps = [step.strip() for step in steps if step.strip()]

print("\nParsed Steps:\n")

for step in steps:
    print(step)

# ==========================================================
# Step 7 : Execute One Step
# ==========================================================

def execute_step(step, previous_results):

    execution_prompt = f"""
            You are an AI Agent.
            
            Previous completed steps:
            
            {previous_results}
            
            Current step:
            
            {step}
            
            Complete ONLY the current step.
            Use previous results if they are helpful.
        """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": execution_prompt
            }
        ]
    )

    return response.choices[0].message.content

# ==========================================================
# Step 8 : Execute Plan
# ==========================================================

results = []
previous_results = ""

for step in steps:

    print(f"\nExecuting : {step}")

    output = execute_step(step, previous_results)

    results.append(output)

    previous_results += f"""

                    Step:
                    {step}
                    
                    Result:
                    {output}
            """

    print("\nResult:\n")
    print(output)

# ==========================================================
# Step 9 : Combine Results
# ==========================================================

combined_results = "\n\n".join(results)

print("\nCombined Results:\n")
print(combined_results)

# ==========================================================
# Step 10 : Reflection
# ==========================================================

reflection_prompt = f"""
You are an AI Reviewer.

The user's original goal was:

{goal}

The AI Agent completed the following steps:

{combined_results}

Create the best final response.

Requirements:
- Combine all useful information.
- Remove repetition.
- Improve clarity.
- Return ONLY the final answer.
"""

reflection_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": reflection_prompt
        }
    ]
)

final_answer = reflection_response.choices[0].message.content

# ==========================================================
# Step 12 : Final Answer
# ==========================================================

print("\n" + "=" * 60)
print("FINAL ANSWER")
print("=" * 60)

print(final_answer)