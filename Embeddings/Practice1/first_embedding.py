from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "I love Python"

embedding = model.encode(text)

print(embedding)
print(type(embedding))
print(len(embedding))