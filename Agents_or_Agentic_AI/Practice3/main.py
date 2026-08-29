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

def get_length(text):
    return len(text)

available_tools = {
    "get_length": get_length
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_length",
            "description": "Get the number of characters in a text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to measure."
                    }
                },
                "required": ["text"]
            }
        }
    }
]


while True:
    goal = input("\nEnter your goal (or type exit): ")

    if goal.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=[
            {
                "role": "user",
                "content": goal
            }
        ],
        tools=tools
    )

    message = response.choices[0].message

    if not message.tool_calls:
        print("\nFinal response:")
        print(message.content)
        continue

    messages = [
        {
            "role": "user",
            "content": goal
        },
        message
    ]


    tool_call = message.tool_calls[0]
    tool_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    print("\nTool name:", tool_name)
    print("Arguments:", arguments)



    if tool_name in available_tools:
        function = available_tools[tool_name]
        result = function(**arguments)
    else:
        result = "Unknown tool"
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    })

    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=messages,
        tools=tools
    )

    print("\nFinal response:")
    print(response.choices[0].message.content)
