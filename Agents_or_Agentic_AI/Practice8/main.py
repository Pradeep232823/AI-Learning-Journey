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


def count_words(text):
    return len(text.split())


def reverse_text(text):
    return text[::-1]


available_actions = {
    "get_length": get_length,
    "count_words": count_words,
    "reverse_text": reverse_text
}



def ask_agent(state):

    prompt = f"""
You are an agent.

Goal:
{state["messages"][-1]["content"]}

Previous observations:
{state["observations"]}

Completed steps:
{state["completed_steps"]}

Available actions:
{list(available_actions.keys())}

Choose the next action required to complete the goal.

Return only JSON:

{{
    "action": "action_name",
    "text": "input text"
}}

If no action is required, return:

{{
    "action": "done",
    "text": ""
}}
"""

    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


agent_state = {
    "messages": [],
    "observations": [],
    "completed_steps": []
}

while True:

    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        break

    agent_state["messages"].append({
        "role": "user",
        "content": user_input
    })

    decision = ask_agent(agent_state)

    print("\nAgent decision:")
    print(decision)

    action = json.loads(decision)

    action_name = action["action"]
    text = action["text"]

    if action_name == "done":
        break

    if action_name not in available_actions:
        print("\nUnsupported action:", action_name)
        continue

    function = available_actions[action_name]

    result = function(text)

    print("\nResult:", result)

    agent_state["observations"].append({
        "action": action_name,
        "text": text,
        "result": result
    })

    agent_state["completed_steps"].append({
        "action": action_name,
        "text": text
    })