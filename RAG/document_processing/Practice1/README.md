# Document Processing RAG System

A simple Retrieval-Augmented Generation (RAG) system built with Python.

This project reads multiple text documents, splits them into sentence-based chunks, generates embeddings for those chunks, stores the embeddings in a JSON file, retrieves relevant chunks for a user query using cosine similarity, and uses an LLM through OpenRouter to generate an answer based only on the retrieved context.

## Project Overview

The system follows this pipeline:

```text
Documents
    ↓
Read text files
    ↓
Sentence-wise chunking
    ↓
Generate embeddings
    ↓
Store vectors in data.json
    ↓
User question
    ↓
Generate query embedding
    ↓
Cosine similarity search
    ↓
Retrieve top-K relevant chunks
    ↓
Build context
    ↓
Send context to LLM
    ↓
Generate final answer
```

## Features

* Read multiple `.txt` documents from the `documents` directory
* Sentence-wise text chunking
* Combine 3 sentences into each chunk
* Generate text embeddings using Sentence Transformers
* Store embeddings and metadata in `data.json`
* Search chunks using cosine similarity
* Retrieve the top-K relevant chunks
* Use a default similarity threshold of `0.5`
* Build context from retrieved chunks
* Generate answers using an LLM through OpenRouter
* Prevent the LLM from using outside knowledge
* Return `"No relevant information"` when no relevant chunks are found
* Interactive question-answering loop

## Project Structure

```text
Practice1/
│
├── documents/
│   ├── fastapi.txt
│   ├── machine_learning.txt
│   └── python.txt
│
├── loader.py
├── indexer.py
├── query.py
├── data.json
├── .env
└── README.md
```

## Modules

### `loader.py`

Contains the main reusable functions and models used by the RAG system.

Responsibilities:

* Load environment variables
* Configure the OpenRouter client
* Load the Sentence Transformer model
* Split text into sentences
* Create sentence-based chunks
* Calculate cosine similarity
* Search the vector store
* Build context for the LLM

Important functions:

```python
sentences_chunks(text, sentences_per_chunk)
```

Splits text into sentences and combines a fixed number of sentences into each chunk.

```python
cosine_similarity(a, b)
```

Calculates the cosine similarity between two vectors.

```python
search_chunks(query, vector_store, top_k, threshold=0.5)
```

Converts the query into an embedding, compares it with stored embeddings, filters results using the similarity threshold, sorts them by score, and returns the top-K results.

```python
build_context(results)
```

Combines the retrieved chunks into a context string for the LLM.

## `indexer.py`

Responsible for creating the vector store.

The process is:

1. Read all files from the `documents` directory.
2. Extract their text.
3. Split each document into sentence-based chunks.
4. Combine 3 sentences into each chunk.
5. Assign a unique chunk ID.
6. Generate embeddings for all chunks.
7. Convert embeddings into JSON-compatible lists.
8. Store the complete vector store in `data.json`.

Each stored vector contains:

```python
{
    "chunk_id": 1,
    "source": "documents/python.txt",
    "text": "...",
    "embedding": [...]
}
```

Run the indexer with:

```bash
python indexer.py
```

## `query.py`

Provides the interactive question-answering system.

The process is:

1. Load `data.json`.
2. Ask the user for a question.
3. Generate an embedding for the question.
4. Search the stored vectors.
5. Retrieve the top-K relevant chunks.
6. Build context from those chunks.
7. Send the context and question to the LLM.
8. Display the generated response.

Run it with:

```bash
python query.py
```

The program continues accepting questions until:

```text
exit
```

is entered.

## Chunking Strategy

This project uses sentence-wise chunking instead of fixed word-based chunking.

The current configuration combines:

```text
3 sentences → 1 chunk
```

For example:

```text
Sentence 1.
Sentence 2.
Sentence 3.
```

becomes:

```text
Chunk 1:
Sentence 1. Sentence 2. Sentence 3.
```

This approach helps keep related sentences together and avoids cutting content in the middle of a sentence.

No chunk overlap is currently used.

## Embeddings

The project uses:

```text
all-MiniLM-L6-v2
```

from Sentence Transformers.

Each chunk is converted into an embedding vector with:

```text
384 dimensions
```

These embeddings are stored in `data.json`.

## Similarity Search

When a user asks a question, the question is converted into an embedding.

The system then calculates cosine similarity between the question embedding and every stored document embedding.

Results are:

1. Filtered using the default threshold of `0.5`
2. Sorted by similarity score
3. Limited to the requested `top_k`

The current query configuration uses:

```python
top_k = 5
```

and:

```python
threshold = 0.5
```

The threshold is intentionally kept fixed rather than dynamically calculated from the retrieved scores.

## Context-Based Generation

Only the retrieved chunks are provided to the LLM.

The prompt instructs the model to:

```text
Answer the question using only the provided context.

If the context does not contain enough information to answer the question,
say "No relevant information found in the documents."

Do not use outside knowledge.
Do not guess or infer missing information.
```

This helps keep the generated answer grounded in the retrieved documents.

## Example Questions

Questions that can be answered from the included documents:

```text
What are Python decorators?
```

```text
What is Python garbage collection?
```

```text
What are the different ways to achieve concurrency in Python?
```

```text
What is FastAPI?
```

```text
What is Machine Learning?
```

For a question that is not covered by the documents:

```text
What is the capital of France?
```

the system should return:

```text
No relevant information
```

## Requirements

Install the required Python packages:

```bash
pip install sentence-transformers openai python-dotenv nltk
```

## Environment Variables

Create a `.env` file in the project directory:

```env
OPENROUTER_API_KEY=your_api_key_here
```

The API key is loaded using `python-dotenv`.

Do not commit the `.env` file to GitHub.

Add it to `.gitignore`:

```text
.env
```

## Running the Project

First, build or update the vector store:

```bash
python indexer.py
```

This creates:

```text
data.json
```

Then start the RAG question-answering system:

```bash
python query.py
```

Example:

```text
Ask a question (or type 'exit'): What is FastAPI?

Response: FastAPI is a modern, high-performance web framework for building APIs with Python...
```

## Technologies Used

* Python
* Sentence Transformers
* `all-MiniLM-L6-v2`
* OpenRouter
* OpenAI Python SDK
* NLTK
* JSON
* python-dotenv

## Key Concepts Practiced

This project demonstrates the basic components of a RAG system:

* Document loading
* Text chunking
* Sentence tokenization
* Embeddings
* Vector storage
* Query embeddings
* Cosine similarity
* Similarity-based retrieval
* Top-K retrieval
* Context construction
* Grounded LLM generation
* Multi-document retrieval
* Interactive question answering

## Limitations

This is a learning-oriented RAG implementation.

Currently:

* Embeddings are stored in a JSON file instead of a dedicated vector database.
* Sentence chunking combines a fixed number of sentences.
* Chunk overlap is not used.
* Similarity search compares the query against every stored vector.
* The similarity threshold is fixed at `0.5`.
* The system currently processes text documents.
* The system depends on an external LLM through OpenRouter for final answer generation.

## Future Improvements

Possible future improvements include:

* Add support for more document formats
* Improve chunking strategies
* Add chunk overlap when appropriate
* Use a dedicated vector database
* Add metadata filtering
* Improve retrieval quality
* Add reranking
* Add a web interface
* Add conversation history
* Add streaming responses
* Add evaluation of retrieval and answer quality

## Learning Outcome

This project demonstrates how a basic RAG pipeline can be built from scratch using Python without relying on a complete RAG framework.

The implementation separates the major stages of the pipeline:

```text
Indexing → Embedding → Storage → Retrieval → Context → Generation
```

This makes it easier to understand how the individual components of a RAG system work together.