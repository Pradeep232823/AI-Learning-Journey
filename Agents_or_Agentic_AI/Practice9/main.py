from openai import OpenAI
from dotenv import load_dotenv
import os
import math

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)


def load_document(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def split_into_chunks(text, chunk_size=2):
    lines = text.splitlines()

    chunks = []

    for i in range(0, len(lines), chunk_size):
        chunk = "\n".join(lines[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

document = load_document("document.txt")

print("\nDocument:")
print(document)

chunks = split_into_chunks(document)

print("\nChunks:")

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)

def create_embedding(text):
    response = client.embeddings.create(
        model="gemini-embedding-001",
        input=text
    )

    return response.data[0].embedding

chunk_embeddings = []

for chunk in chunks:
    embedding = create_embedding(chunk)

    chunk_embeddings.append({
        "text": chunk,
        "embedding": embedding
    })

print("\nEmbedded chunks:", len(chunk_embeddings))

for i, item in enumerate(chunk_embeddings, start=1):
    print(f"Chunk {i} embedding size: {len(item['embedding'])}")

def cosine_similarity(vector_a, vector_b):
    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (magnitude_a * magnitude_b)

def search_chunks(query, chunk_embeddings, top_k=2):
    query_embedding = create_embedding(query)

    results = []

    for item in chunk_embeddings:
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

query = "What is Python commonly used for?"

results = search_chunks(query, chunk_embeddings)

print("\nSearch results:")

for result in results:
    print("\nScore:", result["score"])
    print(result["text"])


def generate_answer(query, results):

    context = "\n\n".join(
        result["text"] for result in results
    )

    prompt = f"""
Answer the user's question using only the provided context.

Context:
{context}

Question:
{query}

If the answer is not present in the context, say:
"I don't know based on the provided document."

Answer:
"""

    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

answer = generate_answer(query, results)

print("\nAnswer:")
print(answer)