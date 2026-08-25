from openai import OpenAI
from dotenv import load_dotenv
import os

from tool_schemas import tools
from tool_executor import execute_tool

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)


messages = [
    {
        "role": "system",
        "content": """
You are an assistant with access to tools.

According to the query must use the available functions.
Do not generate the response yourself.

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
            model="gemini-flash-lite-latest",
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

            # print(f"Tool: {tool_call.function.name}")
            # print(f"Arguments: {tool_call.function.arguments}")
            
            result = execute_tool(tool_call)

            messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })
        try:
            final_response = client.chat.completions.create(
                model="gemini-flash-lite-latest",
                messages=messages,
                tools=tools
            )

            final_message = final_response.choices[0].message

            messages.append(final_message)

            print("Response:", final_message.content)
        except Exception as error:
            print(f"API Error: {error}")

    else:
        messages.append(message)
        print("Response:", message.content)