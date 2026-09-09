from openai import OpenAI
from dotenv import load_dotenv
import os
from models import StudyResponse
from cache import get_cache, set_cache
from tools import calculator
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)


calculator_tool = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Calculate a mathematical expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A mathematical expression such as 25 * 4"
                }
            },
            "required": ["expression"]
        }
    }
}


def ask_ai(text):

    cached = get_cache(text)

    if cached is not None:
        print("Cache hit")
        return cached

    print("Calling Gemini")

    # Step 1: Let Gemini decide whether a tool is needed
    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ],
        tools=[calculator_tool]
    )

    message = response.choices[0].message

    # Step 2: Calculator path
    if message.tool_calls:

        print("Tool call")

        tool_call = message.tool_calls[0]

        arguments = json.loads(tool_call.function.arguments)

        result = calculator(arguments["expression"])

        result = {
            "type": "calculation",
            "data": {
                "result": result
            }
        }

        set_cache(text, result)

        return result

    # Step 3: Study path
    response = client.chat.completions.parse(
        model="gemini-flash-lite-latest",
        messages=[
            {
                "role": "user",
                "content": f"""
Explain this topic:

{text}

Return a short explanation suitable for a learner.
"""
            }
        ],
        response_format=StudyResponse
    )

    study_result = response.choices[0].message.parsed

    result = {
        "type": "study",
        "data": study_result.model_dump()
    }

    set_cache(text, result)

    return result