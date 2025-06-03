import ollama

response = ollama.list()

# Print the ollama models
# print(response)

# ===== Chat example-1 ===== 
res = ollama.chat(
    model="llama3.2",
    messages=[{
        "role": "user", "content": "how old are you?"
    }]
)

# print(res["message"]["content"])

# ===== Chat streaming example-2 ===== 
resp = ollama.chat(
    model="llama3.2",
    messages=[{
        "role": "user", "content": "why is the ocean so salty?"
    }],
    stream=True
)

for chunk in resp:
    print(chunk["message"]["content"], end="", flush=True)