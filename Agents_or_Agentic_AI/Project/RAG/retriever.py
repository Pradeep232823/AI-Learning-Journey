import math

from RAG.embeddings import create_embedding


def cosine_similarity(vector_a, vector_b):

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))

    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (magnitude_a * magnitude_b)


def search_chunks(query, chunk_embeddings, client, top_k=2):

    query_embedding = create_embedding(query, client=client)

    results = []

    for item in chunk_embeddings:

        score = cosine_similarity(query_embedding, item["embedding"])

        results.append({
            "chunk_id": item["chunk_id"],
            "text": item["text"],
            "score": score
        })

    results.sort(key=lambda item: item["score"], reverse=True)

    return results[:top_k]