# Project 02 - Vector Database

## 📖 Overview

This project demonstrates how a Vector Database works internally before using libraries like ChromaDB.

Instead of directly using a Vector Database, we will first build a simple version from scratch using Python.

By the end of this project, we will understand:

- What a Vector Database stores
- How embeddings are generated
- How similarity search works
- How Top-K retrieval works
- Why Vector Databases are needed in RAG
- How ChromaDB performs the same task efficiently

---

## 🎯 Learning Objectives

- Convert documents into embeddings
- Store embeddings in a Python data structure
- Perform similarity search using Cosine Similarity
- Retrieve Top-K most relevant chunks
- Understand the internal working of a Vector Database

---

## 📂 Project Structure

```
02-vector-database/

├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Technologies Used

- Python
- Sentence Transformers
- NumPy
- Scikit-Learn

---

## 📌 Learning Flow

```
Documents
      ↓
Embeddings
      ↓
Store in Python
      ↓
Question
      ↓
Question Embedding
      ↓
Cosine Similarity
      ↓
Top-K Results
```

---

## 📚 Future Improvements

- Replace Python list with ChromaDB
- Store metadata
- Perform faster retrieval using Vector Indexing
- Integrate with an LLM to build a complete RAG application