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

documents = [
    "Python is a programming language.",
    "FastAPI is a Python web framework.",
    "FastAPI can be used to build APIs.",
    "Python is also used for data science."
]

query = "How can I build web APIs using Python?"

retrieved_documents = [
    documents[1],
    documents[2]
]

print("Query:")
print(query)

context = ""

for document in retrieved_documents:
    context += document + "\n"

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