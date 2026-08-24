import json
from loader import search_chunks, build_context, client

with open("data.json", "r", encoding="utf-8") as file:
    vector_store = json.load(file)

question = input("Ask a question: ")

results = search_chunks(question, vector_store, top_k=5)

print(f"\nTop {len(results)} chunks")
print()
for result in results:
    print(f"Chunk {result['chunk_id']} -> Source: {result['source']} -> Text: {result['text']} -> Score: {result['score']:.4f}")


if results:
    context = f"""
Answer the question using only the provided context.

Context:

{build_context(results)}

Question:

{question}
"""
    print(context)

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

    print()
    print("Answer:")
    print(answer)
    print()
else:
    print("No relevant information")