import json
from loader import search_chunks, build_context, client


with open("data.json", "r", encoding="utf-8") as file:
    vector_store = json.load(file)


def ask_question(query, top_k):

    results = search_chunks(
        query,
        vector_store,
        top_k
    )

    if not results:
        return "No relevant information found in the documents."

    context = f"""
Answer the question using only the provided context.

If the context does not contain enough information to answer the question,
say "No relevant information found in the documents."

Do not use outside knowledge.
Do not guess or infer missing information.

Context:

{build_context(results)}

Question:

{query}
"""

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": context
            }
        ]
    )

    answer = response.choices[0].message.content

    return answer


while True:

    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    top_k = 5

    result = ask_question(query, top_k)

    print(f"\nResponse: {result}")