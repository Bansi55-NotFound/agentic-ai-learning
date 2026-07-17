from huggingface_hub import InferenceClient

client = InferenceClient(
    token="your-token"
)

response = client.chat_completion(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Explain Transformers in one sentence."
        }
    ]
)

print(response.choices[0].message.content)