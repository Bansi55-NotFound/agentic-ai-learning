# Project 11 - SmolAgents

## Overview

This project demonstrates the fundamentals of building AI agents using **SmolAgents**, a lightweight framework developed by Hugging Face.

Unlike traditional LLM applications that simply generate text, SmolAgents allow an LLM to reason, write Python code, execute it, use external tools, and return the final answer.

---

## Topics Covered

- CodeAgent
- InferenceClientModel
- Python Code Execution
- Built-in Tools
- Custom Tools
- Web Search using DuckDuckGo
- Multi-Step Reasoning
- Mini Research Assistant Project

---

## Project Structure

```
11-smolagents/
│
├── app.py              # Basic CodeAgent example
├── web_search.py       # DuckDuckGo Search Tool
├── reasoning.py        # Multi-step reasoning example
├── mini_project.py     # AI Research Assistant
├── requirements.txt
└── README.md
```

---

## Concepts Learned

### 1. CodeAgent

A CodeAgent generates Python code, executes it, observes the results, and produces the final response.

### 2. Python Execution

Instead of directly answering, the LLM can solve problems by writing and executing Python code.

### 3. Built-in Tools

SmolAgents provide built-in tools such as:

- DuckDuckGoSearchTool
- VisitWebpageTool
- Python Interpreter

### 4. Web Search

The agent can search the web whenever external information is required.

### 5. Multi-Step Reasoning

The agent automatically breaks complex problems into smaller steps before generating the final answer.

---

## Learning Outcomes

After completing this project, I understood:

- How SmolAgents work internally
- How CodeAgent differs from traditional chatbots
- How AI agents reason before answering
- How tools are integrated into an agent
- How web search improves responses
- How to build lightweight AI agents with minimal code

---

## Technologies Used

- Python
- SmolAgents
- Hugging Face Inference API
- DuckDuckGo Search
- dotenv

---

## Author

Bansi Sapariya