import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5:1.5b",
    "prompt": "Who are you?",
    "stream": False
}

response = requests.post(url, json=payload)

print(response.json()["response"])