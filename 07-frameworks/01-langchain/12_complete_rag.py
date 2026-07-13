"""
============================================================
PROJECT 07 : LANGCHAIN

Example 12 : Complete RAG Application

============================================================
"""

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# ==========================================================
# Step 1 : Load PDF
# ==========================================================

loader = PyPDFLoader("sample.pdf")

documents = loader.load()

# ==========================================================
# Step 2 : Split Documents
# ==========================================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

# ==========================================================
# Step 3 : Embedding Model
# ==========================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==========================================================
# Step 4 : Create Vector Store
# ==========================================================

vector_store = FAISS.from_documents(
    chunks,
    embedding_model
)

# ==========================================================
# Step 5 : Retriever
# ==========================================================

retriever = vector_store.as_retriever()

# ==========================================================
# Step 6 : LLM
# ==========================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# ==========================================================
# Step 7 : Chat Loop
# ==========================================================

while True:

    question = input("\nQuestion : ")

    if question.lower() == "exit":
        break

    # Search Relevant Documents
    docs = retriever.invoke(question)

    # Build Context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # Prompt
    prompt = f"""
Answer using ONLY the following context.

Context:
{context}

Question:
{question}
"""

    # LLM
    response = llm.invoke(prompt)

    print("\nAnswer:\n")

    print(response.content)