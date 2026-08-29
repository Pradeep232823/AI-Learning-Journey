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

def load_conversation(filename = "conversations.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"\nError: {filename} does not contain valid JSON.")
        return []


def save_conversation(conversation, filename = "conversations.json"):
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(conversation, file, indent=4)


conversation = load_conversation()
MAX_MESSAGES = 6

while True:
    goal = input("\nYou: ")

    if goal.lower() == "exit":
        break

    conversation.append({
        "role": "user",
        "content": goal
    })


    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=conversation,
    )

    answer = response.choices[0].message.content

    print("\nAgent:", answer)

    conversation.append({
        "role": "assistant",
        "content": answer
    })
    
    if len(conversation) > MAX_MESSAGES:
        conversation = conversation[-MAX_MESSAGES:]

    save_conversation(conversation)