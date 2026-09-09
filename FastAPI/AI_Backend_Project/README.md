````markdown
# AI Backend Project – Study Assistant API

A FastAPI-based AI backend that provides structured study explanations and performs mathematical calculations using Gemini function calling.

This project demonstrates important AI backend engineering concepts including:

- FastAPI
- Pydantic
- Structured Outputs
- Function Calling
- Error Handling
- Caching
- Safe Tool Execution
- Gemini API integration through the OpenAI SDK

---

## Features

### 1. AI Study Assistant

Send a topic and receive a structured response containing:

- Topic
- Summary
- Difficulty
- Key points

Example:

{
    "topic": "Python functions"
}
````

Response:

```json
{
    "type": "study",
    "data": {
        "topic": "Python functions",
        "summary": "Functions are reusable blocks of code...",
        "difficulty": "Beginner",
        "key_points": [
            "Functions are defined using def",
            "Functions can accept parameters",
            "Functions can return values"
        ]
    }
}
```

---

### 2. Function Calling

The AI can decide when a calculator tool is required.

Example:

```text
Calculate (23 + 5) * 2
```

Gemini generates a tool call:

```json
{
    "expression": "(23 + 5) * 2"
}
```

The backend then executes the calculator locally and returns:

```json
{
    "type": "calculation",
    "data": {
        "result": 56
    }
}
```

This demonstrates the basic AI function-calling workflow:

```text
User Request
     ↓
Gemini
     ↓
Tool Call
     ↓
Calculator
     ↓
Tool Result
     ↓
API Response
```

---

## Safe Calculator Tool

The calculator does not use Python's `eval()`.

Instead, it uses Python's `ast` module to parse mathematical expressions and explicitly allows only supported operators.

Supported operators:

* Addition `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`
* Power `**`

Examples:

```text
23 + 4
23 + 5 * 2
(23 + 5) * 2
100 / (5 + 5)
```

Invalid expressions and division by zero are handled safely.

---

## Structured Outputs

Study responses are generated using a Pydantic model:

```python
class StudyResponse(BaseModel):
    topic: str
    summary: str
    difficulty: str
    key_points: list[str]
```

This ensures that the AI response follows a predictable structure instead of returning arbitrary text.

---

## Caching

The application includes a simple in-memory cache.

Before calling Gemini:

```text
Request
   ↓
Check Cache
   ↓
Cache Hit → Return Cached Result
   ↓
Cache Miss
   ↓
Call Gemini
   ↓
Store Result in Cache
```

Repeated requests for the same input avoid another AI API call.

Example console output:

```text
Calling Gemini
```

First request:

```text
Explain Python functions
```

Repeated request:

```text
Cache hit
```

---

## API

### POST `/study`

Main endpoint for study questions and calculations.

#### Request

```json
{
    "topic": "Explain Python functions"
}
```

#### Study Response

```json
{
    "type": "study",
    "data": {
        "topic": "Python functions",
        "summary": "...",
        "difficulty": "Beginner",
        "key_points": [
            "...",
            "...",
            "..."
        ]
    }
}
```

#### Calculation Request

```json
{
    "topic": "Calculate 25 * 4"
}
```

#### Calculation Response

```json
{
    "type": "calculation",
    "data": {
        "result": 100
    }
}
```

---

## Error Handling

The API validates incoming requests using Pydantic.

For example, an empty topic is rejected.

The backend also catches AI service errors and returns:

```json
{
    "detail": "AI service temporarily unavailable"
}
```

---

## Project Structure

```text
AI_Backend_Project/
│
├── ai_service.py
├── cache.py
├── main.py
├── models.py
├── tools.py
├── README.md
└── .env
```

### File Responsibilities

#### `main.py`

Defines the FastAPI application and API endpoint.

#### `ai_service.py`

Handles:

* Gemini API connection
* Tool calling
* Structured study responses
* Cache integration
* AI request flow

#### `models.py`

Contains Pydantic models for:

* Request validation
* Study responses
* API result structure

#### `tools.py`

Contains the safe calculator tool.

#### `cache.py`

Contains the in-memory caching functions.

---

## Architecture

```text
                    ┌───────────────┐
                    │     Client    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    FastAPI    │
                    │   /study      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │     Cache     │
                    └───────┬───────┘
                            │
                       Cache Miss
                            │
                            ▼
                    ┌───────────────┐
                    │    Gemini     │
                    └───────┬───────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
             Tool Call             No Tool
                 │                     │
                 ▼                     ▼
          ┌─────────────┐       ┌──────────────┐
          │ Calculator  │       │ StudyResponse│
          └──────┬──────┘       └──────┬───────┘
                 │                     │
                 └──────────┬──────────┘
                            ▼
                     Store in Cache
                            │
                            ▼
                       API Response
```

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* OpenAI Python SDK
* Gemini API
* python-dotenv
* AST
* Git & GitHub

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit the `.env` file to GitHub.

---

## How to Run

Install the required dependencies:

```bash
pip install fastapi uvicorn openai python-dotenv pydantic
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Example Requests

### Study

```json
{
    "topic": "Explain Python classes"
}
```

### Calculation

```json
{
    "topic": "Calculate (23 + 5) * 2"
}
```

### Invalid Calculation

```json
{
    "topic": "Calculate 10 / 0"
}
```

The calculator safely handles division by zero.

---

## Key Engineering Concepts Learned

This project demonstrates:

1. Building an AI API with FastAPI
2. Request validation with Pydantic
3. Structured AI responses
4. LLM function calling
5. Executing AI-selected tools
6. Safe mathematical expression evaluation
7. Error handling
8. Basic response caching
9. Environment variable management
10. Separating API, AI service, models, tools, and cache responsibilities

---

## Future Improvements

Possible future improvements include:

* Persistent caching
* More AI tools
* Authentication
* Database integration
* Better logging
* Streaming responses
* More advanced AI workflows
* Deployment

---

## Project Status

**Completed**

This project was built as part of an AI Engineering learning journey to practice backend AI application development and core AI engineering patterns.