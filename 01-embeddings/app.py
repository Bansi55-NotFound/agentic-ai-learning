"""
============================================================
PROJECT 1 : EMBEDDINGS
============================================================

Objective
---------
Understand how an embedding model converts text into vectors
and how we can compare the semantic similarity between
sentences.

Model Used
----------
all-MiniLM-L6-v2

Concepts Covered
----------------
1. Loading an embedding model
2. Generating embeddings
3. Cosine Similarity
4. Understanding embedding vectors

Author Notes
------------
This file will continue to grow throughout the course.
Each example builds on the previous one.
Nothing will be deleted—only new concepts will be added.

============================================================
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ============================================================
# Step 1 : Load the Embedding Model
# ============================================================

print("=" * 70)
print("Loading Embedding Model...")
print("=" * 70)

model = SentenceTransformer("all-MiniLM-L6-v2")

print("✅ Model Loaded Successfully!")

# ============================================================
# Example 1 : Compare Similarity Between Sentences
# ============================================================

print("\n")
print("=" * 70)
print("EXAMPLE 1 : COSINE SIMILARITY")
print("=" * 70)

# Sample Sentences

sentences = [
    "I love Python programming.",
    "Python is an amazing programming language.",
    "I enjoy playing football."
]

# Generate embeddings

embeddings = model.encode(sentences)

# Display information about the returned object

print("\nType of embeddings object")
print(type(embeddings))

print("\nShape of embeddings")
print(embeddings.shape)

"""
Expected Shape

(3, 384)

Meaning

3   -> Number of sentences

384 -> Dimensions for each embedding
"""

# Compare Sentence 1 and Sentence 2

similarity_python = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)

# Compare Sentence 1 and Sentence 3

similarity_football = cosine_similarity(
    [embeddings[0]],
    [embeddings[2]]
)

print("\nSimilarity Scores")

print("\nPython ↔ Python")
print(similarity_python)

print("\nPython ↔ Football")
print(similarity_football)

"""
Observation

Sentence 1 and Sentence 2 have similar meaning.

Therefore,
Cosine Similarity is high.

Sentence 1 and Sentence 3 discuss different topics.

Therefore,
Cosine Similarity is much lower.
"""

# ============================================================
# Example 2 : Understanding Embedding Vectors
# ============================================================

print("\n")
print("=" * 70)
print("EXAMPLE 2 : UNDERSTANDING EMBEDDINGS")
print("=" * 70)

sentence = "I love Python"

embedding = model.encode(sentence)

print("\nSentence")
print(sentence)

print("\nType")
print(type(embedding))

print("\nShape")
print(embedding.shape)

print("\nEmbedding Dimension")
print(len(embedding))

print("\nData Type")
print(embedding.dtype)

print("\nFirst 10 Values")

print(embedding[:10])

"""
Observation

Every sentence becomes a NumPy array.

This model converts every sentence into
a 384-dimensional vector.

Each value is a floating-point number.

The values themselves don't have human-readable meaning.

Together,
all 384 numbers represent the semantic meaning
of the sentence.
"""

# ============================================================
# Summary
# ============================================================

print("\n")
print("=" * 70)
print("SUMMARY")
print("=" * 70)

print("""
✔ Loaded an Embedding Model
✔ Converted Text into Embeddings
✔ Compared Sentence Similarity
✔ Understood Embedding Dimensions
✔ Observed NumPy Array Output

Next:
We will generate embeddings for multiple sentences
and understand why the shape becomes (N, 384).
""")

# ============================================================
# Example 3 : Multiple Sentence Embeddings
# ============================================================

sentences1 = [
    "I love Python programming.",
    "Python is an amazing programming language.",
    "I enjoy playing football.",
    "AI is the future.",
    "I Love AI and I will use it."
]
print("=" * 70)
print(sentences1)
embeddings1 = model.encode(sentences1)

print("Type embedding: ", type(embeddings1))
print("embedding shape: ", embeddings1.shape)
print("type embedding[0]: ", type(embeddings1[0]))
print("embedding[0].shape :", embeddings1[0].shape)
print("embedding[0][:5]: ", embeddings1[0][:5])