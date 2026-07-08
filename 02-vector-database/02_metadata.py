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

for index, (doc, embedding) in enumerate(zip(documents, embeddings), start=1):

    vector_db.append(
        {
            "id": index,
            "text": doc,
            "embedding": embedding,
            "metadata": {
                "source": "Employee Handbook",
                "page": 1,
                "chunk_id": index
            }
        }
    )

print("\nVector DB Created Successfully!")

print("\nFirst Record:\n")

print(f"ID        : {vector_db[0]['id']}")
print(f"Text      : {vector_db[0]['text']}")
print(f"Source    : {vector_db[0]['metadata']['source']}")
print(f"Page      : {vector_db[0]['metadata']['page']}")
print(f"Chunk ID  : {vector_db[0]['metadata']['chunk_id']}")
print(f"Embedding : {len(vector_db[0]['embedding'])} Dimensions")

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
            "score": similarity,
            "metadata": record["metadata"]
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

    print("=" * 50)
    print(f"Similarity Score : {result['score']:.4f}")
    print(f"Document         : {result['text']}")
    print(f"Source           : {result['metadata']['source']}")
    print(f"Page             : {result['metadata']['page']}")
    print(f"Chunk ID         : {result['metadata']['chunk_id']}")
    print("=" * 50)
    print()