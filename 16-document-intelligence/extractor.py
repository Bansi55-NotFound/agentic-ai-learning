# ============================================================
# Project 16 - AI Document Intelligence
#
# File: extractor.py
#
# Purpose:
# Extract text from a PDF document.
# ============================================================

from langchain_community.document_loaders import PyPDFLoader


# ============================================================
# Extract Text
# ============================================================

def extract_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF document.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A single string containing the text from all pages.
    """

    # Load PDF
    loader = PyPDFLoader(pdf_path)

    # Read all pages
    pages = loader.load()

    # Combine page contents
    text = "\n\n".join(page.page_content for page in pages)

    return text