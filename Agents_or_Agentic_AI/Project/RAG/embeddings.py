def create_embedding(text, client):
    response = client.embeddings.create(
        model="gemini-embedding-001",
        input=text
    )

    return response.data[0].embedding