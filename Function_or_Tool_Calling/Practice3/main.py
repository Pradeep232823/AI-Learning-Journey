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
    if isinstance(km, (int, float)):
        return km*1000
    return "Invalid value"

def km_to_miles(km):
    if isinstance(km, (int, float)):
        return km * 0.621371
    return "Invalid Value"

def celsius_to_fahrenheit(celsius):
    if isinstance(celsius, (int, float)):
        return (celsius * 9 / 5) + 32
    return "Invalid value"

def kg_to_grams(kg):
    if isinstance(kg, (int, float)):
        return kg * 1000
    return "Invalid value"

def kg_to_pounds(kg):
    if isinstance(kg, (int, float)):
        return kg * 2.20462
    return "Invalid value"



available_tools = {
    "km_to_m": km_to_m,
    "km_to_miles": km_to_miles,
    "celsius_to_fahrenheit": celsius_to_fahrenheit,
    "kg_to_grams": kg_to_grams,
    "kg_to_pounds": kg_to_pounds
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
    },
    {
        "type": "function",
        "function": {
            "name": "km_to_miles",
            "description": "Convert a distance from kilometers to miles.",
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
    },
    {
        "type": "function",
        "function": {
            "name": "celsius_to_fahrenheit",
            "description": "Convert a temperature from celsius to fahrenheit.",
            "parameters": {
                "type": "object",
                "properties": {
                    "celsius": {
                        "type": "number",
                        "description": "The temperature in celsius."
                    }
                },
                "required": ["celsius"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "kg_to_grams",
            "description": "Convert a weight kilograms to grams",
            "parameters": {
                "type": "object",
                "properties": {
                    "kg": {
                        "type": "number",
                        "description": "The weight in kilograms."
                    }
                },
                "required": ["kg"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "kg_to_pounds",
            "description": "Convert a weight from kilograms to pounds.",
            "parameters": {
                "type": "object",
                "properties": {
                    "kg": {
                        "type": "number",
                        "description": "The weight in kilograms."
                    }
                },
                "required": ["kg"]
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
    query = input("Asq query (or type 'exit'): ")

    if query.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": query
    })

    try:
        response = client.chat.completions.create(
            model="models/gemini-flash-lite-latest",
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
            model="models/gemini-flash-lite-latest",
            messages=messages,
            tools=tools
        )

        print("Response:", final_response.choices[0].message.content)

    else:
        messages.append(message)
        print("Response:", message.content)