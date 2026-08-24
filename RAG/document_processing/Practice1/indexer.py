from loader import sentences_chunks, model
import os
import json

directory = "documents"

files = os.listdir(directory)

file_paths = []

for filename in files:
    file_paths.append(os.path.join(directory, filename))

files_data = []

for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        files_data.append({
            "source": file_path,
            "text": content
        })

chunks_data = []

chunk_id = 1

for file_data in files_data:
    chunks = sentences_chunks(file_data["text"], 3)

    for chunk in chunks:
        chunks_data.append(
            {
                "chunk_id": chunk_id,
                "source": file_data["source"],
                "text": chunk
            }
        )

        chunk_id += 1

chunk_texts = [chunk['text'] for chunk in chunks_data]

embeddings = model.encode(chunk_texts)

vector_store = []

for chunk, embedding in zip(chunks_data, embeddings):
    vector_store.append({
        "chunk_id": chunk["chunk_id"],
        "source": chunk["source"],
        "text": chunk["text"],
        "embedding": embedding.tolist()
    })

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(vector_store, file, indent=4)