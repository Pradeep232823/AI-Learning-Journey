from sentence_transformers import SentenceTransformer
from math import sqrt
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not configured")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Python is a programming language.",
    "FastAPI is a Python web framework.",
    "FastAPI can be used to build APIs.",
    "Python is also used for data science."
]

embeddings = model.encode(documents)

vector_store = []

for document, embedding in zip(documents, embeddings):
    vector_store.append({
        "text": document,
        "embedding": embedding
    })

print("Number of stored documents:", len(vector_store))

def cosine_similarity(a, b):

    if len(a) != len(b):
        raise ValueError("Both vectors should be same length")

    dot_product = 0
    length_a = 0
    length_b = 0

    for i in range(len(a)):
        dot_product += a[i] * b[i]

    for value in a:
        length_a += value * value

    for value in b:
        length_b += value * value

    if length_a == 0 or length_b == 0:
        raise ValueError("Cannot calculate similarity for a zero vector")

    return dot_product / (sqrt(length_a) * sqrt(length_b))

def search_documents(query, top_k):

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


def build_context(results):

    context = ""

    for result in results:
        context += result["text"] + "\n"

    return context

query = "How can I build web APIs using Python?"

results = search_documents(
    query,
    top_k=2
)

context = build_context(results)

print()
print("Context:")
print(context)

prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{query}
"""

print()
print("Prompt:")
print(prompt)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

answer = response.choices[0].message.content

print()
print("Answer:")
print(answer)