# Agentic AI - RAG + Tool + Memory

A Python-based Agentic AI project that combines **RAG (Retrieval-Augmented Generation)**, **tool usage**, and **conversation memory**.

The agent decides where the answer should come from based on the user's query and previous conversation history.

---

## Features

- 🤖 LLM-based decision-making agent
- 📚 RAG-based document question answering
- 🧮 Calculator tool for arithmetic operations
- 🧠 Conversation memory
- 🔄 Follow-up calculations using previous results
- ➕ Supports multiple mathematical expressions
- 🧮 Supports operator precedence
- 🔢 Supports decimal numbers
- `( )` Supports parentheses
- ❌ Handles invalid mathematical expressions
- 🚫 Handles division by zero
- 💾 Saves conversation history to JSON
- 🔐 Uses environment variables for API keys
- ⚠️ Handles API quota/rate-limit errors gracefully
- 🧩 Modular project structure

---

## Project Architecture

The application has three main decision paths:

```text
                    User Query
                        |
                        v
                  +-------------+
                  |    Agent    |
                  +-------------+
                        |
              +---------+---------+
              |         |         |
              v         v         v
             RAG       TOOL     MEMORY
              |         |         |
              v         v         v
          Document   Calculator  Previous
          Search                 Conversation
              |         |         |
              +---------+---------+
                        |
                        v
                   Final Answer
````

---

## How the Agent Works

The agent receives:

* User query
* Available tools
* Previous conversations

It then decides whether the answer should come from:

### 1. RAG

Used when the required information should come from the provided document.

Example:

```text
User: What is Python?
```

The agent selects:

```json
{
    "action": "retrieve",
    "source": "rag",
    "text": ""
}
```

The relevant document chunks are retrieved and passed to the generator.

---

### 2. TOOL

Used when the user requests a calculation.

The agent extracts and normalizes the mathematical expression.

For example:

```text
23+2
```

becomes:

```text
23 + 2
```

Natural-language calculations are also supported:

```text
what is 24 plus 6
```

becomes:

```text
24 + 6
```

For calculations based on the previous result:

```text
23 + 2
```

Result:

```text
25.0
```

Then:

```text
add 5
```

becomes:

```text
25.0 + 5
```

The calculator then produces:

```text
30.0
```

---

### 3. MEMORY

Used when the requested information already exists in the conversation history.

Example:

```text
User: 23 + 2
Answer: 25.0

User: What was the result?
```

The agent retrieves the previous answer from conversation memory:

```text
25.0
```

---

## Calculator Capabilities

The calculator supports:

### Addition

```text
23 + 5
23+5
```

### Subtraction

```text
100 - 5
100-5
```

### Multiplication

```text
10 * 5
10*5
```

### Division

```text
100 / 4
100/4
```

### Decimal numbers

```text
10.5 + 2.5
10.5 * 2
100.5 / 2
```

### Multiple expressions

```text
10 + 5 * 2
10 + 5 * 2 + 10
100 / 5 + 10
10 / 2 / 5
```

### Parentheses

```text
(10 + 5) * 2
100 / (5 + 5)
(23 + 5) * 2
```

The calculator uses Python's `ast` module to safely parse mathematical expressions instead of directly evaluating arbitrary Python code.

Supported operators:

```text
+
-
*
/
```

---

## Error Handling

Invalid expressions are handled without crashing the calculator.

Example:

```text
23 + abc
```

Output:

```text
Invalid mathematical expression
```

Division by zero:

```text
100 / 0
```

Output:

```text
Can't divide using 0
```

The application also handles Gemini API quota/rate-limit errors using exception handling so that an API failure does not unnecessarily terminate the application with a traceback.

---

## RAG Pipeline

The RAG pipeline follows these steps:

```text
document.txt
     |
     v
Load Document
     |
     v
Split Into Chunks
     |
     v
Create Embeddings
     |
     v
Store Chunk + Embedding
     |
     v
User Query
     |
     v
Search Relevant Chunks
     |
     v
Generate Answer
```

The project separates the RAG functionality into different modules for easier maintenance.

---

## Conversation Memory

Conversation history is maintained during the application session.

Example:

```text
Question 1: 23 + 2
Answer 1: 25.0

Question 2: add 5
Answer 2: 30.0

Question 3: multiply by 2
Answer 3: 60.0
```

This allows follow-up calculations such as:

```text
23 + 2
add 5
multiply by 2
divide by 4
subtract 3
```

The latest successful numeric result is used for follow-up calculations.

---

## Conversation Persistence

Conversation data is also saved in JSON format.

Example:

```json
[
    {
        "Question 1": "23 + 2",
        "Expression": "23 + 2",
        "Answer 1": "25.0"
    },
    {
        "Question 2": "add 5",
        "Expression": "25.0 + 5",
        "Answer 2": "30.0"
    }
]
```

This provides a record of the interaction and the expressions used by the calculator.

---

## Project Structure

```text
Project/
│
├── Agent/
│   ├── __init__.py
│   └── agent.py
│
├── RAG/
│   ├── __init__.py
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── generator.py
│
├── Tools/
│   ├── __init__.py
│   ├── calculator.py
│   └── registry.py
│
├── document.txt
├── main.py
├── conversations.json
├── requirements.txt
├── .env
└── .gitignore
```

> `conversations.json` is generated by the application if conversation persistence is enabled.

---

## Module Responsibilities

### `main.py`

Responsible for:

* Application startup
* Loading the document
* Creating embeddings
* Initializing the agent
* Receiving user input
* Processing agent decisions
* Maintaining conversation history
* Saving conversation data
* Running the main application loop

---

### `Agent/agent.py`

Responsible for:

* Agent decision-making
* RAG / Tool / Memory routing
* Parsing agent JSON responses
* Validating agent responses
* Generating tool answers
* Generating RAG answers
* Executing registered tools

---

### `RAG/loader.py`

Responsible for loading the document.

---

### `RAG/chunker.py`

Responsible for splitting the document into smaller chunks.

---

### `RAG/embeddings.py`

Responsible for creating embeddings for document chunks.

---

### `RAG/retriever.py`

Responsible for finding relevant document chunks for a user query.

---

### `RAG/generator.py`

Responsible for generating the final answer using the retrieved context.

---

### `Tools/calculator.py`

Responsible for performing mathematical calculations.

It supports:

* Addition
* Subtraction
* Multiplication
* Division
* Decimal numbers
* Parentheses
* Multiple expressions
* Operator precedence

---

### `Tools/registry.py`

Maintains the available tools and allows the agent to access them.

---

## Technologies Used

* Python
* OpenAI Python SDK
* Google Gemini API
* python-dotenv
* JSON
* `ast`
* `operator`

The OpenAI Python SDK is used with Gemini's OpenAI-compatible API endpoint.

---

## Environment Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not hard-code API keys inside Python files.

---

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run:

```bash
python main.py
```

The application will ask:

```text
Enter your query (or type exit):
```

Type:

```text
exit
```

to stop the application.

---

## Example Usage

### Calculator

```text
Enter your query (or type exit): 23 + 2

Answer: 25.0
```

### Follow-up calculation

```text
Enter your query (or type exit): 23 + 2

Answer: 25.0

Enter your query (or type exit): add 5

Answer: 30.0

Enter your query (or type exit): multiply by 2

Answer: 60.0
```

### RAG

```text
Enter your query (or type exit): what is python?

Answer:
Based on the provided context, Python is a high-level, general-purpose programming language...
```

### RAG follow-up

```text
Enter your query (or type exit): when was it released?

Answer:
Python was first released in 1991.
```

### Memory

```text
Enter your query (or type exit): 23 + 2

Answer: 25.0

Enter your query (or type exit): what was the result?

Answer: 25.0
```

---

## Testing

The project was tested with:

### Basic calculations

```text
23 + 3
23+3
100-5
100 - 5
10*5
100/4
```

### Natural-language calculations

```text
what is 24 plus 6
calculate 100 divided by 5
```

### Operator precedence

```text
10 + 5 * 2
10 - 2 * 3
100 / 5 + 10
```

### Parentheses

```text
(10 + 5) * 2
100 / (5 + 5)
(23 + 5) * 2
```

### Decimal calculations

```text
10.5 + 2.5
10.5 * 2
100.5 / 2
```

### Invalid expressions

```text
23 + g
23 + abc
hello + world
23 +
23 *
```

### Division by zero

```text
10 / 0
100 / (5 - 5)
10 + 5 / 0
```

### Conversation memory

```text
23 + 2
add 5
multiply by 2
divide by 4
subtract 3
what was the result
```

### RAG

```text
what is python
when was it released
who created it
is it dynamically typed
tell me about python again
```

### Unknown document information

```text
What is the capital of France?
What is the population of Python?
```

The system responds that the information is not available in the provided document.

---

## Security

The calculator does not use Python's `eval()` for expression execution.

Instead, expressions are parsed using:

```python
ast.parse(expression, mode="eval")
```

Only supported numeric constants and mathematical operators are evaluated.

API keys are stored in `.env` and excluded from Git using `.gitignore`.

---

## Git Ignore

Sensitive and generated files should not be committed.

Example:

```gitignore
.env
API Keys.txt
__pycache__/
*.pyc
rough.py
.venv/
venv/
.git/
.pytest_cache/
Notes/
```

---

## Limitations

* The application depends on the Gemini API.
* API rate limits can temporarily prevent requests.
* RAG answers depend on the information available in `document.txt`.
* Conversation memory is limited to the conversation data maintained by the application.
* Agent routing is LLM-based and therefore may occasionally make an incorrect routing decision.
* Natural-language mathematical expressions depend on the agent correctly extracting the expression.

---

## Future Improvements

Possible future improvements include:

* Add more tools
* Add a weather tool
* Add a web-search tool
* Add file-based RAG for multiple documents
* Add persistent long-term memory
* Add automated unit tests
* Add structured logging
* Add retry/backoff for API rate limits
* Add a CLI interface
* Add a web interface
* Improve agent routing with structured outputs
* Add more mathematical operations

---

## Learning Goals

This project demonstrates the core concepts of Agentic AI:

```text
LLM
 ↓
Decision Making
 ↓
Tool Selection
 ↓
Tool Execution
 ↓
RAG Retrieval
 ↓
Conversation Memory
 ↓
Final Response
```

The main goal is to understand how an AI agent can **decide which capability should handle a user's request instead of directly answering every request itself**.