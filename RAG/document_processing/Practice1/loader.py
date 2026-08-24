from sentence_transformers import SentenceTransformer
from math import sqrt
from openai import OpenAI
from dotenv import load_dotenv
import os
from nltk.tokenize import sent_tokenize


load_dotenv()


api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not configured")


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


model = SentenceTransformer("all-MiniLM-L6-v2")


def load_text(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")


def sentences_chunks(text, sentences_per_chunk):

    sentences = sent_tokenize(text)

    chunks = []
    chunk_text = ""

    for i, sentence in enumerate(sentences, start=1):

        chunk_text += sentence + " "

        if i % sentences_per_chunk == 0:
            chunks.append(chunk_text.strip())
            chunk_text = ""

    if chunk_text.strip():
        chunks.append(chunk_text.strip())

    return chunks


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


def search_chunks(query, vector_store, top_k, threshold=0.5):

    query_embedding = model.encode(query)

    results = []

    for item in vector_store:

        score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        if score >= threshold:
            results.append({
                "chunk_id": item["chunk_id"],
                "source": item["source"],
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

        context_entry = (
            f"source: {result['source']}\n"
            f"chunk_id: {result['chunk_id']}\n"
            f"text: {result['text']}\n"
        )

        context += context_entry

    return context