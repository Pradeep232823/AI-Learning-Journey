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


def ask_agent(prompt):
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

    max_iterations = 5
    iteration = 0
    completed_actions = []
    observation = ""
    final_answer= ""

    while iteration < max_iterations:
        decision_prompt = f"""
You are an agent

User goal:
{goal}

Previous observation:
{observation}

Available actions:
{actions}

Completed Actions:
{completed_actions}

Decide what should happen next.
IMPORTANT:
The final answer must only contain results that were actually produced
by the available actions.

Do not perform calculations or transformations yourself.

If the user requested an operation that is not available,
do not include a result for that operation.
Clearly state that the operation is unsupported.

Return JSON:

{{
    "action": "action_name",
    "text": "text to give the action"
}}

If all requested tasks that can be completed have been completed,
return:

{{
    "action": "done",
    "text": "final answer"
}}
"""
        action = parse_response(ask_agent(decision_prompt))
        print(action)

        if action["action"].strip() == "done":
            final_answer = action["text"]
            break

        action_name = action["action"]
        function = actions[action_name]
        text = action["text"]

        result = function(text)
        print(f"Step {iteration+1} Result: {result}")

        iteration+=1

        completed_actions.append({
            "action": action_name,
            "text": text,
            "result": result
        })
        
        observation = result

    if iteration >= max_iterations and not final_answer:
        print("\nAgent stopped: maximum iterations reached.")
        continue
    print("\nFinal Answer:",final_answer)