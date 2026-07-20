# 🤖 AI Data Engineering Assistant

An AI-powered Data Engineering Assistant built using **LangChain**, **Groq Llama 3.3**, and **Streamlit**.

This application acts as a personal AI mentor for Data Engineers. It can answer Data Engineering questions, generate SQL and PySpark code, explain Spark concepts, assist with ETL design, and maintain conversation context using chat memory.

---

## 🚀 Features

- 💬 ChatGPT-style chat interface
- 🧠 Conversation memory
- 🐍 PySpark code generation
- 🗄️ SQL query generation
- ⚡ Apache Spark concept explanations
- 📊 Databricks and Delta Lake guidance
- ☁️ Azure Data Engineering assistance
- 🏗️ ETL pipeline recommendations
- 🎯 Data Engineering interview preparation
- 📝 Professional prompt engineering

---

## 🛠️ Tech Stack

- Python
- LangChain
- LangChain Core
- Groq (Llama 3.3 70B)
- Streamlit
- Python Dotenv

---

## 📂 Project Structure

```
17-ai-data-engineering-assistant/
│
├── app.py
├── assistant.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
└── images/
    └── demo.png
```

---

## ⚙️ How It Works

```
              User
                │
                ▼
      Streamlit Chat Interface
                │
                ▼
      Conversation History
                │
                ▼
      System Prompt + History
                │
                ▼
          Groq Llama 3.3
                │
                ▼
          AI Response
```

The assistant remembers previous messages during the session, allowing users to ask follow-up questions naturally.

---

## ▶️ Installation

### Clone the repository

```bash
git clone <your-repository-url>
```

### Navigate to the project

```bash
cd 17-ai-data-engineering-assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

### Run the application

```bash
streamlit run app.py
```

---

## 💬 Example Questions

### SQL

- Write SQL to find duplicate records.
- Find the second highest salary.
- Explain GROUP BY vs HAVING.

### PySpark

- Convert this SQL query to PySpark.
- Remove duplicate records using PySpark.
- Explain broadcast join.

### Apache Spark

- Difference between repartition and coalesce.
- What is lazy evaluation?
- Explain Spark architecture.

### Databricks

- Explain Delta Lake.
- What is Unity Catalog?
- Difference between Delta Table and Parquet.

### Azure

- Explain ADLS Gen2.
- What is Azure Data Factory?
- How does Databricks integrate with ADLS?

### ETL

- Generate a PySpark ETL pipeline.
- Explain schema drift.
- Design a data pipeline for customer transactions.

### Interview Preparation

- Ask me PySpark interview questions.
- Explain Spark optimizations.
- Generate Data Engineering interview questions.

---

## 📸 Demo

![demo.png](images/demo.png)

---

## 🎯 Learning Outcomes

This project demonstrates:

- Prompt Engineering
- LangChain Chains
- Conversation Memory
- ChatPromptTemplate
- MessagesPlaceholder
- HumanMessage and AIMessage
- Streamlit Chat Components
- LLM Integration with Groq
- Production-ready AI Chat Applications

---

## 🔮 Future Improvements

- Conversation persistence using a database
- Upload SQL files for analysis
- Generate PySpark notebooks
- Connect to Databricks APIs
- Execute SQL against sample databases
- Support multiple LLM providers
- Export conversations
- Authentication and user accounts

---

## 👨‍💻 Author

Built as part of my AI Engineering learning journey to combine Generative AI with real-world Data Engineering use cases.