from sentence_transformers import SentenceTransformer
from math import sqrt


def cosine_similarity(a, b):

    if len(a) != len(b):
        return "Both vectors should be same length"

    dot_product = 0

    for i in range(len(a)):
        dot_product += a[i] * b[i]

    length_a = 0
    length_b = 0

    for i in a:
        length_a += i * i

    for i in b:
        length_b += i * i

    if length_a == 0 or length_b == 0:
        return "Cannot calculate similarity for a zero vector"

    return dot_product / (sqrt(length_a) * sqrt(length_b))


model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Python is a programming language.",
    "FastAPI is a Python web framework.",
    "The Earth revolves around the Sun.",
    "Python supports object-oriented programming."
]

query = "How can I build web APIs using Python?"

document_embeddings = model.encode(documents)
query_embedding = model.encode(query)

results = []

for document, embedding in zip(documents, document_embeddings):
    score = cosine_similarity(query_embedding, embedding)
    results.append((document, score))

results.sort(key=lambda x: x[1], reverse=True)
top_results = results[:2]
print("Query:", query)
print()

for document, score in top_results:
    print(f"{score:.4f} - {document}")