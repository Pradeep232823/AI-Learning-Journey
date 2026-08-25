from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not configured")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b

available_tools = {
    "add_numbers": add_numbers,
    "subtract_numbers": subtract_numbers,
    "multiply_numbers": multiply_numbers,
    "divide_numbers": divide_numbers
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Add two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "The first number"
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "subtract_numbers",
            "description": "Subtract the second number from the first number.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "The first number"
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiply_numbers",
            "description": "Multiply two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "The first number"
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "divide_numbers",
            "description": "Divide the first number by the second number.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "The first number"
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
]

def execute_tool(tool_call):
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    if function_name not in available_tools:
        return f"Unknown tool: {function_name}"

    function = available_tools[function_name]

    return function(**arguments)

messages = [
    {
        "role": "system",
        "content": """
You are an assistant with access to tools.

For any arithmetic calculation, you must use an available tool.
Do not calculate arithmetic yourself.

Only use tools that are provided.
If a required operation does not have an available tool, tell the user that the operation is not supported.
"""
    }
]

while True:
    query = input("Ask something (or type 'exit'): ")

    if query.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": query
    })

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=tools
    )

    message = response.choices[0].message

    if message.tool_calls:

        messages.append(message)

        for tool_call in message.tool_calls:
            result = execute_tool(tool_call)

            messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })

        final_response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=tools
        )

        print("Response:", final_response.choices[0].message.content)

    else:
        messages.append(message)
        print("Response:", message.content)