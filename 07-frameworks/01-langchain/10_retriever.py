from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# ==================================================
# Step 1 : Embedding Model
# ==================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==================================================
# Step 2 : Documents
# ==================================================

documents = [
    "Python is a programming language.",
    "Machine Learning is a subset of AI.",
    "Databricks is used for Big Data.",
    "Azure is a cloud platform."
]

# ==================================================
# Step 3 : Vector Store
# ==================================================

vector_store = FAISS.from_texts(
    documents,
    embedding_model
)

# ==================================================
# Step 4 : Create Retriever
# ==================================================

retriever = vector_store.as_retriever()

# ==================================================
# Step 5 : Search
# ==================================================

results = retriever.invoke(
    "What is Machine Learning?"
)

print(results)