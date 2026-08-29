from openai import OpenAI, APIConnectionError
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

actions = {
    "get_length": get_length,
    "count_words": count_words,
    "reverse_text": reverse_text
}

def ask_agent(prompt):
    try:
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
    except APIConnectionError as e:
        print(f"Problem while connection: {e}")
        exit()
    

def parse_response(response_content):
    response_content = response_content.strip()

    if response_content.startswith("```"):
        response_content = response_content.replace("```json", "")
        response_content = response_content.replace("```", "")
        response_content = response_content.strip()

    try:
        return json.loads(response_content)
    except json.JSONDecodeError:
        return {
                "actions" : [
                    {
                        "action": "none",
                        "text": ""
                    }
                ]
            }



while True:

    goal = input("\nEnter your goal (or type exit): ").strip()

    if goal == "exit":
        break

    if not goal:
        print("Please enter a goal.")
        continue

    decision_prompt = f"""
You are an agent that analyzes a user's goal and creates an action plan.

User goal:
{goal}

Available actions:
{actions}

Your job is to identify every requested action in the user's goal
and validate each action before returning the plan.

VALIDATION RULES:

1. The user must request at least one action.

2. Each requested action must clearly match one of the available actions.

3. The user may use different natural-language phrases for an action.

   Examples:
   - "count words in hello world" → count_words
   - "how many words are in hello world" → count_words
   - "words in hello world" → count_words

   - "length of hello world" → get_length
   - "how long is hello world" → get_length
   - "count characters in hello world" → get_length

   - "reverse hello world" → reverse_text
   - "hello world in reverse" → reverse_text

4. Do NOT guess or invent an action.

   If a requested operation cannot clearly be mapped to one of
   the available actions, that action is INVALID.

   Example:
   User:
   "reverse hello world and hugrigh"

   Result:
   - reverse hello world → valid
   - hugrigh → invalid

   Return:
   {{
       "actions": [
           {{
               "action": "reverse_text",
               "text": "hello world"
           }},
           {{
               "action": "none",
               "text": ""
           }}
       ]
   }}

5. Validate the input/data for every action.

   An action is INVALID if:
   - the action is unknown
   - the required text is missing
   - the requested operation has no meaningful input
   - the text cannot be determined from the user's request

6. If the user requests multiple actions, validate EACH action
   independently.

   Example:
   "reverse hello world and count words in Python is easy"

   Return:
   {{
       "actions": [
           {{
               "action": "reverse_text",
               "text": "hello world"
           }},
           {{
               "action": "count_words",
               "text": "Python is easy"
           }}
       ]
   }}

7. If one action is invalid, DO NOT convert it into a valid action
   just because another available action could be applied to its text.

8. Do not execute any action. Only create the action plan.

9. Return ONLY valid JSON.

OUTPUT FORMAT:

{{
    "actions": [
        {{
            "action": "action_name",
            "text": "input text"
        }}
    ]
}}

For an invalid action:

{{
    "actions": [
        {{
            "action": "none",
            "text": ""
        }}
    ]
}}

For a completely unsupported goal:

{{
    "actions": [
        {{
            "action": "none",
            "text": ""
        }}
    ]
}}
"""

    response_content = ask_agent(decision_prompt)

    data = parse_response(response_content)

    actions_plan = data["actions"]

    for action in actions_plan:
        if action["action"] == "none":
            print("\nUser input has incomplete goal.")
            break
    else:
        current_text = None

        for action in actions_plan:
            action_name = action["action"]
            text = action["text"]

            if current_text is not None:
                text = current_text

            result = actions[action_name](text)

            print(f"\nAction: {action_name}")
            print(f"Input: {text}")
            print(f"Result: {result}")

            current_text = result