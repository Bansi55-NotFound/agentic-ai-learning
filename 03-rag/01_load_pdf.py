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