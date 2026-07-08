# Project 03 - Retrieval Augmented Generation (RAG)

## 📖 Overview

This project builds a complete RAG pipeline from scratch.

We will:

- Load a PDF
- Extract text
- Split text into chunks
- Generate embeddings
- Store embeddings in ChromaDB
- Retrieve the most relevant chunks
- Send the retrieved context to an LLM
- Generate the final answer

---

## 📂 Project Structure

```
03-rag/

├── 01_load_pdf.py
├── 02_chunking.py
├── 03_embeddings.py
├── 04_chromadb.py
├── 05_retrieval.py
├── 06_rag.py
```

---

## Learning Pipeline

```
PDF
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Retrieval
    ↓
LLM
    ↓
Answer
```