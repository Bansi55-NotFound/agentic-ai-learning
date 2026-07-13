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
    "Artificial Intelligence enables machines to think.",
    "Machine Learning is a subset of AI.",
    "Databricks is used for big data processing."
]

# ==================================================
# Step 3 : Create Vector Store
# ==================================================

vector_store = FAISS.from_texts(
    texts=documents,
    embedding=embedding_model
)

print("Vector Store Created Successfully!")