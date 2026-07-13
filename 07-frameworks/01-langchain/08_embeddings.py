from langchain_huggingface import HuggingFaceEmbeddings

# ==================================================
# Step 1 : Embedding Model
# ==================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==================================================
# Step 2 : Text
# ==================================================

text = "Artificial Intelligence"

# ==================================================
# Step 3 : Generate Embedding
# ==================================================

embedding = embedding_model.embed_query(text)

print("Embedding Dimension :")

print(len(embedding))

print("\nFirst 10 Values:\n")

print(embedding[:10])