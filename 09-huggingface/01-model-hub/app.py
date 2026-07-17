"""
Module 01 - Hugging Face Model Hub

This file demonstrates how to interact with the Hugging Face Model Hub
using the `huggingface_hub` library.

Topics Covered:
1. Search models
2. Fetch model metadata
3. List repository files
4. Filter models by task
"""

from huggingface_hub import (
    list_models,
    model_info,
    list_repo_files,
)

# ==========================================================
# 1. Search Models
# ==========================================================
print("=" * 60)
print("1. Search Models")
print("=" * 60)

# Search for the first 10 models containing the keyword "llama"
models = list_models(search="llama", limit=10)

for model in models:
    print(model.id)


# ==========================================================
# 2. Fetch Model Information
# ==========================================================
print("\n" + "=" * 60)
print("2. Model Information")
print("=" * 60)

# Retrieve metadata for a specific model
info = model_info("Qwen/Qwen2.5-1.5B-Instruct")

print(f"Model      : {info.id}")
print(f"Downloads  : {info.downloads}")
print(f"Likes      : {info.likes}")
print(f"Task       : {info.pipeline_tag}")
print(f"License    : {info.card_data.get('license')}")


# ==========================================================
# 3. List Repository Files
# ==========================================================
print("\n" + "=" * 60)
print("3. Repository Files")
print("=" * 60)

# Display all files available inside the model repository
files = list_repo_files("Qwen/Qwen2.5-1.5B-Instruct")

for file in files:
    print(file)


# ==========================================================
# 4. Filter Models by Task
# ==========================================================
print("\n" + "=" * 60)
print("4. Filter Models by Task (Text Generation)")
print("=" * 60)

# Search only for models that support text generation
text_generation_models = list_models(
    filter="text-generation",
    limit=10,
)

for model in text_generation_models:
    print(model.id)