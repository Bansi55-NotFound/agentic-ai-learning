# ----------------------------------------------------
# Import required libraries
# ----------------------------------------------------
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# ----------------------------------------------------
# Load environment variables (.env)
# This loads the GROQ_API_KEY
# ----------------------------------------------------
load_dotenv()

# ----------------------------------------------------
# Step 1: Load the same embedding model used
# during ingestion.
#
# IMPORTANT:
# Query embeddings and document embeddings
# must use the SAME embedding model.
# ----------------------------------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ----------------------------------------------------
# Step 2: Load the existing Chroma database
#
# We are NOT creating embeddings again.
# We are simply reopening the stored database.
# ----------------------------------------------------
vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model,
)

# ----------------------------------------------------
# Step 3: Create the retriever
#
# k=3 means retrieve the 3 most relevant chunks.
# ----------------------------------------------------
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)

# ----------------------------------------------------
# Step 4: Initialize the Groq LLM
#
# temperature=0
# Gives more deterministic and factual answers.
# ----------------------------------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ----------------------------------------------------
# Step 5: Create the prompt template
#
# {context} -> Retrieved chunks
# {question} -> User's question
# ----------------------------------------------------
prompt = ChatPromptTemplate.from_template(
    """
You are an HR assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
reply with:
"I couldn't find that information in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""
)

# ----------------------------------------------------
# Helper function
#
# Converts retrieved Document objects into
# a single string before sending to the LLM.
# ----------------------------------------------------
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# ----------------------------------------------------
# Step 6: Build the RAG Chain
#
# Flow:
#
# User Question
#       ↓
# Retriever
#       ↓
# Relevant Chunks
#       ↓
# Prompt
#       ↓
# Groq LLM
#       ↓
# Final Answer
# ----------------------------------------------------
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)

# ----------------------------------------------------
# Function to answer user questions
#
# This function will be used by both:
# 1. Terminal
# 2. Streamlit UI
# ----------------------------------------------------
def ask_question(question: str) -> str:
    """
    Takes a user question and returns the chatbot response.
    """
    return rag_chain.invoke(question)


# ----------------------------------------------------
# Run only when rag.py is executed directly
#
# If another file (like app.py) imports rag.py,
# this block will NOT execute.
# ----------------------------------------------------
if __name__ == "__main__":

    print("=" * 60)
    print("📚 Employee Handbook Chatbot")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        answer = ask_question(question)

        print("\nBot:")
        print(answer)