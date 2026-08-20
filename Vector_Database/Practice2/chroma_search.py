import chromadb

client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_or_create_collection(name="documents_metadata")

def add_documents():
    if collection.count() == 0:

        documents = [
            "Python is a programming language.",
            "FastAPI is a Python web framework.",
            "The Earth revolves around the Sun.",
            "Python supports object-oriented programming."
        ]

        metadatas = [
            {"topic": "programming"},
            {"topic": "web"},
            {"topic": "science"},
            {"topic": "programming"}
        ]

        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=["doc1", "doc2", "doc3", "doc4"]
        )

        print("Documents added successfully")

    else:
        print("Documents already exist")


    print("Number of documents:", collection.count())

def get_documents():
    data = collection.get()

    return data

def search_documents(query):

    results = collection.query(
        query_texts=[query],
        n_results=3,
        where={
            "$or": [
                {"topic": "programming"},
                {"topic": "web"}
            ]
        }
    )

    return results
          
def update_document(doc, content):
    collection.update(
        ids=[doc],
        documents=[content]
    )

    print("Document updated")

    data = collection.get(
        ids=[doc]
    )

    return data

def delete_document(doc):
    collection.delete(
        ids=[doc]
    )

    print("Document deleted")

    print("Number of documents:", collection.count())

    data = get_documents()

    return data

if __name__ == "__main__":

    add_documents()

    data = get_documents()
    print(data)

    results = search_documents(
        "How can I build web APIs using Python?"
    )
    print(results)