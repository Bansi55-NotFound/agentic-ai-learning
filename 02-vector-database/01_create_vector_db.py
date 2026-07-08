"""
============================================================
PROJECT 02 : VECTOR DATABASE
============================================================

Goal:
Understand how a Vector Database works internally before
using libraries like ChromaDB.

In this project we will:

1. Create document chunks
2. Convert chunks into embeddings
3. Store them in a Python data structure
4. Perform similarity search
5. Retrieve Top-K results

============================================================
"""

"""
============================================================
PROJECT 02 : VECTOR DATABASE
============================================================

Goal:
Build a mini Vector Database from scratch.

Workflow:
Documents
    ↓
Embeddings
    ↓
Store in Python
    ↓
Similarity Search
    ↓
Top-K Retrieval

============================================================
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ==========================================================
# Step 1 : Load Embedding Model
# ==========================================================

model = SentenceTransformer("all-MiniLM-L6-v2")
# ==========================================================
# Step 2 : Create Document Chunks
# ==========================================================

documents = [
    "Employees receive 24 paid leaves annually.",
    "Leave requests require manager approval.",
    "Health insurance covers employees and families.",
    "Travel expenses are reimbursed by the company.",
    "Employees can work from home three days a week."
]

print("Documents:\n")

for doc in documents:
    print(doc)

# ==========================================================
# Step 3 : Generate Embeddings
# ==========================================================

embeddings = model.encode(documents)

print("\nEmbedding Shape:", embeddings.shape)

# ==========================================================
# Step 4 : Build Mini Vector Database
# ==========================================================

vector_db = []

for doc, embedding in zip(documents, embeddings):

    vector_db.append({
        "text": doc,
        "embedding": embedding
    })

print("\nVector DB Created Successfully!")

print("\nFirst Record:\n")

print("Text:")
print(vector_db[0]["text"])

print("\nEmbedding Dimension:")
print(len(vector_db[0]["embedding"]))

print("\nFirst 5 values:")
print(vector_db[0]["embedding"][:5])

# ==========================================================
# Step 5 : User Question
# ==========================================================

question = "How many paid leaves do employees get?"

question_embedding = model.encode(question)

print("\nQuestion:")
print(question)

print("\nQuestion Embedding Shape:")
print(question_embedding.shape)

# ==========================================================
# Step 6 : Retrieve Top-K Documents
# ==========================================================

similarity_scores = []

for record in vector_db:

    similarity = cosine_similarity(
        [question_embedding],
        [record["embedding"]]
    )[0][0]

    similarity_scores.append(
        {
            "text": record["text"],
            "score": similarity
        }
    )

# Sort documents based on similarity score (Highest First)

similarity_scores = sorted(
    similarity_scores,
    key=lambda x: x["score"],
    reverse=True
)

print("\nTop 2 Results:\n")

for result in similarity_scores[:2]:

    print(f"Score : {result['score']:.4f}")
    print(result["text"])
    print()