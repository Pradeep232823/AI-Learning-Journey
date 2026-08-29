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

def get_plan(goal):

    prompt = f"""
Extract all operations requested in the user's goal.

Goal:
{goal}

Available actions:
{list(available_actions.keys())}

Return every requested operation in the original order.

Map each supported operation to the exact action name from Available actions.

For example:
- "count words" → "count_words"
- "count characters" → "get_length"
- "reverse" → "reverse_text"

If an operation is not supported by Available actions,
keep the user's operation as the action name.

Include unsupported operations too.

Do not execute any operation.
Do not calculate any result.

Return only JSON:

{{
    "steps": [
        {{
            "action": "action_name",
            "text": "input text"
        }}
    ]
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
            "steps": []
        }

while True:

    goal = input("\nEnter your goal (or type exit): ").strip()

    if goal.lower() == "exit":
        break

    agent_state = {
        "goal": goal,
        "plan": [],
        "observations": [],
        "completed_steps": [],
        "skipped_steps": [],
        "goal_status": "Not completed"
    }

    try:

        plan_response = get_plan(goal)
        plan = parse_response(plan_response)

        agent_state["plan"] = plan["steps"]

    except (KeyError, TypeError):

        print("\nCould not create a valid plan.")
        continue

    if not agent_state["plan"]:

        print("\nNo operations found.")
        continue

    print("\nPlan:")

    for index, step in enumerate(agent_state["plan"], start=1):

        print(
            f"{index}. "
            f"{step['action']} "
            f"-> {step['text']}"
        )

    for step in agent_state["plan"]:

        action_name = step["action"]
        text = step["text"]

        if action_name not in available_actions:

            print(
                f"\nUnsupported action: {action_name}"
            )

            agent_state["skipped_steps"].append(step)

            continue

        function = available_actions[action_name]

        result = function(text)


        print(
            f"\nAction Name: {action_name}"
            f"\nText: {text}"
            f"\nResult: {result}"
        )

        agent_state["observations"].append({
            "action": action_name,
            "text": text,
            "result": result
        })

        agent_state["completed_steps"].append(step)

    if agent_state["skipped_steps"]:
        agent_state["goal_status"] = "Completed with skipped operations"
    else:
        agent_state["goal_status"] = "Completed"

    print("\nAll planned operations handled.")

    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=[
            {
                "role": "user",
                "content": f"""
                Generate the final response from the agent state below.

                Agent state:
                {agent_state}

                Rules:
                - Use only results present in observations.
                - Do not perform any new calculation or transformation.
                - Do not invent results.
                - Mention unsupported operations from skipped_steps.
                - Clearly summarize the completed results and skipped operations.
                """
            }
        ]
    )
    
    final_result = response.choices[0].message.content

    print("\nFinal Result:")

    print(final_result)