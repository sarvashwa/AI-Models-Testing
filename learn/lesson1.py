import json

with open("sample_response.json") as f:
    data = json.load(f)

content = data["choices"][0]["message"]["content"]
tokens = data["usage"]["total_tokens"]
model = data["model"]

print(f"[{model}] {content}")
print(f"Tokens used: {tokens}")