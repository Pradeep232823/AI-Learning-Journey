def generate_answer(query, results, conversations, client):

    context = "\n\n".join(
        result["text"] for result in results
    )

    prompt = f"""
Answer the user's question using only the provided context.

Context:
{context}

Question:
{query}

Previous Conversations:
{conversations}

Use the retrieved document context to answer.
Use previous conversation only to understand references
and follow-up questions.
If the answer is not supported by the document,
say you don't know based on the provided document.

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