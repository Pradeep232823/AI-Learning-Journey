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

document = """
Python is a programming language.
It is widely used for web development.
FastAPI is a modern Python web framework.
It can be used to build APIs.
Python is also used for data science.
Machine learning is another common application.
"""

def word_chunks(text, chunk_size, overlap):

    words = text.split()

    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0")

    if overlap < 0:
        raise ValueError("Overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size")

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = words[start:end]

        chunks.append(" ".join(chunk))

        start = end - overlap

    return chunks


chunks = word_chunks(
    document.strip(),
    chunk_size=10,
    overlap=2
)

embeddings = model.encode(chunks)

print()
print("Number of chunks:", len(chunks))
print("Embedding dimensions:", len(embeddings[0]))

vector_store = []

for chunk, embedding in zip(chunks, embeddings):
    vector_store.append({
        "text": chunk,
        "embedding": embedding
    })

print("Number of stored chunks:", len(vector_store))


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


def search_chunks(query, top_k):

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

results = search_chunks(
    query,
    top_k=2
)

print()
print("Query:", query)
print()

for result in results:
    print(f"{result['score']:.4f} - {result['text']}")

def build_context(results):

    context = ""

    for result in results:
        context += result["text"] + "\n"

    return context

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