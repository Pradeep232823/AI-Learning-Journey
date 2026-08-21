from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# tokenizer = model.tokenizer

# text = "Python is a programming language."

# tokens = tokenizer.tokenize(text)

# print(tokens)
# print("Number of tokens:", len(tokens))

# print()

# def chunk_text(text, chunk_size, overlap):

#     if chunk_size <= 0:
#         raise ValueError("Chunk size must be greater than 0")

#     if overlap < 0:
#         raise ValueError("Overlap cannot be negative")

#     if overlap >= chunk_size:
#         raise ValueError("Overlap must be smaller than chunk size")

#     chunks = []

#     start = 0

#     while start < len(text):
#         end = start + chunk_size

#         chunk = text[start:end]
#         chunks.append(chunk)

#         start = end - overlap

#     return chunks


document = """
Python is a programming language.
It is widely used for web development.
FastAPI is a modern Python web framework.
It can be used to build APIs.
Python is also used for data science.
Machine learning is another common application.
"""

# chunks = chunk_text(
#     document.strip(),
#     chunk_size=100,
#     overlap=20
# )

# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i + 1}:")
#     print(chunk)
#     print()

# try:
#     chunks = chunk_text(
#         document.strip(),
#         chunk_size=100,
#         overlap=100
#     )
# except ValueError as error:
#     print(error)
#     print()

# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i + 1}:")
#     print(chunk)
#     print()

# try:
#     chunks = chunk_text(
#         document.strip(),
#         chunk_size=100,
#         overlap=-5
#     )

#     for i, chunk in enumerate(chunks):
#         print(f"Chunk {i + 1}:")
#         print(chunk)
#         print()

# except ValueError as error:
#     print(error)
#     print()

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
print()

vector_store = []

for chunk, embedding in zip(chunks, embeddings):

    vector_store.append({
        "text": chunk,
        "embedding": embedding
    })

print("Number of stored chunks:", len(vector_store))
print()

from math import sqrt


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

def search_chunks(query, top_k, threshold):

    query_embedding = model.encode(query)

    results = []

    for item in vector_store:

        score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        if score >= threshold:
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
    top_k=2,
    threshold=0.5
)

for result in results:
    print(f"{result['score']:.4f} - {result['text']}")