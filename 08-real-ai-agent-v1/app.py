"""
============================================================
PROJECT 08 : REAL AI AGENT

Main

============================================================
"""

from graph import app

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    state = {

        "question": question,

        "tool": "",

        "a": 0,

        "b": 0,

        "result": 0,

        "answer": ""
    }

    app.invoke(state)