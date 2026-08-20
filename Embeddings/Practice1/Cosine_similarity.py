from math import sqrt
from sentence_transformers import SentenceTransformer
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

    score = dot_product/(sqrt(length_a) * sqrt(length_b))
    return score


model = SentenceTransformer("all-MiniLM-L6-v2")

text_a = "I love Python"
text_b = "I enjoy programming in Python"
text_c = "The weather is very cold today"

embedding_a = model.encode(text_a)
embedding_b = model.encode(text_b)
embedding_c = model.encode(text_c)

similarity = cosine_similarity(embedding_a, embedding_b)
similarity2 = cosine_similarity(embedding_a, embedding_c)

print("Similarity-1:", similarity)
print("Similarity-2:", similarity2)