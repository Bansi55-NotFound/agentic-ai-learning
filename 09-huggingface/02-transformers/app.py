from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "distilgpt2"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Input text
text = "Artificial Intelligence is"

# Convert text to token IDs
inputs = tokenizer(text, return_tensors="pt")

# Generate new tokens
output_ids = model.generate(
    **inputs,
    max_new_tokens=50
)

# Convert token IDs back to text
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print(output_text)