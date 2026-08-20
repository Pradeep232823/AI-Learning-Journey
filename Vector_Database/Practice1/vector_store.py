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

embeddings = model.encode(documents)

vector_store = []

for document, embedding in zip(documents, embeddings):
    vector_store.append({
        "text": document,
        "embedding": embedding
    })

print("Number of stored documents:", len(vector_store))

def search(query, top_k = 2):

    query_embedding = model.encode(query)

    results = []

    for item in vector_store:
        score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        results.append({
            "text": item["text"],
            "score": score
        })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:top_k]


query = "How can I build web APIs using Python?"

results = search(query)

for result in results:
    print(f"{result['score']:.4f} - {result['text']}")