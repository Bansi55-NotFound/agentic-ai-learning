import chromadb
"""
============================================================
PROJECT 03 : RAG
Example 1 : Load PDF
============================================================

Goal:
Learn how to read text from a PDF.

Workflow:

PDF
    ↓
Read Pages
    ↓
Extract Text

============================================================
"""

# ==========================================
# Example 1 : Basic Chunking
# ==========================================

from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key="YOUR_API_KEY")

# ==========================================================
# Step 1 : Load PDF
# ==========================================================

pdf_path = "employee_handbook.pdf"

reader = PdfReader(pdf_path)

print(f"Total Pages : {len(reader.pages)}")

# ==========================================================
# Step 2 : Extract Text from PDF
# ==========================================================

print("\nExtracted Text:\n")

text = reader.pages[0].extract_text()

print(text)

# ==========================================================
# Step 3 : Split Text into Chunks
# ==========================================================

chunk_size = 100

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

print(f"\nTotal Chunks Created: {len(chunks)}")
print("\nGenerated Chunks:\n")

for index, chunk in enumerate(chunks, start=1):
    print(f"Chunk {index}")
    print("-" * 40)
    print(chunk)
    print()


# ==========================================
# Example 2 : Overlapping Chunking
# ==========================================

# ==========================================================
# Example 2 : Overlapping Chunking
# ==========================================================

chunk_size = 100
overlap = 20

overlap_chunks = []

start = 0

while start < len(text):

    end = start + chunk_size

    chunk = text[start:end]

    overlap_chunks.append(chunk)

    start += chunk_size - overlap

print(f"\nTotal Overlapping Chunks : {len(overlap_chunks)}")

print("\nGenerated Overlapping Chunks:\n")

for index, chunk in enumerate(overlap_chunks, start=1):

    print(f"Chunk {index}")
    print("-" * 50)
    print(chunk)
    print()

# ==========================================================
# Example 3 : Generate Embeddings for Chunks
# ==========================================================

model = SentenceTransformer("all-MiniLM-L6-v2")

chunk_embeddings = model.encode(overlap_chunks)

print("\nEmbedding Shape :", chunk_embeddings.shape)

print("\nFirst Chunk Embedding Dimension :", len(chunk_embeddings[0]))

print("\nFirst 5 Values of First Chunk Embedding:")

print(chunk_embeddings[0][:5])

# ==========================================================
# Example 4 : Store Chunks in ChromaDB
# ==========================================================

client = chromadb.Client()

collection = client.create_collection(
    name="employee_handbook"
)

print("\nCollection Created Successfully!")

collection.add(
    documents=overlap_chunks,

    embeddings=chunk_embeddings.tolist(),

    ids=[
        f"chunk_{i}"
        for i in range(len(overlap_chunks))
    ],

    metadatas=[
        {
            "source": "employee_handbook.pdf",
            "chunk": i + 1
        }
        for i in range(len(overlap_chunks))
    ]
)

print("Chunks Stored Successfully!")

# ==========================================================
# Example 5 : Retrieve Relevant Chunks
# ==========================================================

question = "How many paid leaves do employees receive?"

question_embedding = model.encode(question)

results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=2
)

print("\nTop Retrieved Chunks:\n")

for i in range(len(results["documents"][0])):

    print("=" * 50)

    print(f"Chunk : {results['metadatas'][0][i]['chunk']}")
    print(f"Source: {results['metadatas'][0][i]['source']}")

    print("\nContent:")
    print(results["documents"][0][i])

    print("=" * 50)
    print()

# ==========================================================
# Example 6 : Build Context
# ==========================================================

client = genai.Client(api_key=api_key)

context = "\n\n".join(results["documents"][0])

print("\nRetrieved Context:\n")
print(context)

# ==========================================================
# Example 7 : Create Prompt
# ==========================================================

prompt = f"""
You are a helpful assistant.

Answer the user's question ONLY using the context below.

Context:
{context}

Question:
{question}
"""

# ==========================================================
# Example 8 : Generate Answer
# ==========================================================

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\nFinal Answer:\n")

print(response.text)