from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)

def km_to_m(km):
    if isinstance(km, int) or isinstance(km, float):
        return km*1000
    return "Invalid value"

available_tools = {
    "km_to_m": km_to_m
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "km_to_m",
            "description": "Convert a distance from kilometers to meters.",
            "parameters": {
                "type": "object",
                "properties": {
                    "km": {
                        "type": "number",
                        "description": "The distance in kilometers."
                    }
                },
                "required": ["km"]
            }
        }
    }
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

For any value conversions, you must use an available tool.
Do not convert yourself.

Only use tools that are provided.
If a required operation does not have an available tool, tell the user that the operation is not supported.
"""
    }
]

while True:
    query = input("Enter value in Kilometers to convert (or type 'exit'): ")

    if query.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": query
    })

    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages,
            tools=tools
        )
    except Exception as error:
        print(f"API error: {error}")
        continue

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
            model="gemini-2.5-flash",
            messages=messages,
            tools=tools
        )

        print("Response:", final_response.choices[0].message.content)

    else:
        messages.append(message)
        print("Response:", message.content)