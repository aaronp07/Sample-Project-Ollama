import ollama

# Save the Modelfile to disk
with open("Modelfile", "w") as f:
    f.write("""
            FROM llama3.2
            SYSTEM You are very smart assistant who knows everything about oceans. You are very sccinct and informative.
            PARAMETER temperature 0.1
            """)

# Create a new model using the file path
ollama.model_create(name="knowitall", modelfile="Modelfile")

# Generate a response
res = ollama.generate(model="knowitall", prompt="why is the ocean so salty?")

print(res["response"])

# Delete model 'Modelfile' from ollama list
ollama.delete("knowitall")