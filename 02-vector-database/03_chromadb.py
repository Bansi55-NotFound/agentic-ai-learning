"""
============================================================
PROJECT 02 : VECTOR DATABASE
Example 3 : ChromaDB
============================================================

Goal:
Replace our manual Python list with ChromaDB and
understand how a real Vector Database works.

Workflow:

Documents
    ↓
Embeddings
    ↓
Store in ChromaDB
    ↓
Question
    ↓
Question Embedding
    ↓
Retrieve Top-K Documents

============================================================
"""

from sentence_transformers import SentenceTransformer
import chromadb

# ==========================================================
# Step 1 : Load Embedding Model
# ==========================================================

model = SentenceTransformer("all-MiniLM-L6-v2")

# ==========================================================
# Step 2 : Create ChromaDB Client
# ==========================================================

#The client is simply our connection to the Vector Database.
client = chromadb.Client()

# ==========================================================
# Step 3 : Create Collection
# ==========================================================

'''A Collection is simply a container that stores:

Documents
Embeddings
Metadata
IDs

Just like a table in SQL stores rows.'''

collection = client.create_collection(
    name="employee_handbook"
)

print("Collection Created Successfully!")

# ==========================================================
# Step 4 : Create Document Chunks
# ==========================================================

documents = [
    "Employees receive 24 paid leaves annually.",
    "Leave requests require manager approval.",
    "Health insurance covers employees and families.",
    "Travel expenses are reimbursed by the company.",
    "Employees can work from home three days a week."
]

# ==========================================================
# Step 5 : Store Documents in ChromaDB
# ==========================================================
# Generate embeddings using our own model
embeddings = model.encode(documents)

collection.add(
    documents=documents,

    embeddings=embeddings.tolist(),

    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4",
        "doc5"
    ],

    metadatas=[
        {"source": "Employee Handbook", "page": 1},
        {"source": "Employee Handbook", "page": 2},
        {"source": "Employee Handbook", "page": 3},
        {"source": "Employee Handbook", "page": 4},
        {"source": "Employee Handbook", "page": 5},
    ]
)
print("Documents Stored Successfully!")

# ==========================================================
# Step 6 : Query ChromaDB
# ==========================================================

question = "How many paid leaves do employees get?"

question_embedding = model.encode(question)

results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=2
)

print("\nTop 2 Results:\n")

for i in range(len(results["documents"][0])):

    print("=" * 50)

    print(f"Document : {results['documents'][0][i]}")
    print(f"Source   : {results['metadatas'][0][i]['source']}")
    print(f"Page     : {results['metadatas'][0][i]['page']}")
    print(f"Distance : {results['distances'][0][i]:.4f}")

    print("=" * 50)
    print()