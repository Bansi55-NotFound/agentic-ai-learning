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