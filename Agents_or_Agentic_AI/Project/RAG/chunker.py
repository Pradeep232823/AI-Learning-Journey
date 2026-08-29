def split_into_chunks(text, chunk_size=2):
    paragraphs = text.splitlines()

    chunks = []

    for i in range(0, len(paragraphs), chunk_size):
        chunk = "\n".join(paragraphs[i:i + chunk_size])
        chunks.append(chunk)

    return chunks