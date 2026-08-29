from openai import OpenAI
from dotenv import load_dotenv
import os
import re
import math

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)

def check_divisibility(number):
    results = {}

    limit = int(math.sqrt(number))

    for divisor in range(2, limit + 1):
        results[divisor] = number % divisor == 0

    return results

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

def execute_action(action_name, number):
    if action_name not in actions:
        return "Unknown action"

    if action_name == "check_divisibility":
        return actions[action_name](number)

    return "Action requires different arguments"

def extract_number(goal):
    match = re.search(r"\b\d+\b", goal)

    if not match:
        return None

    return int(match.group())



actions = {
    "check_divisibility": check_divisibility
}



agent_state = {
    "goal": "",
    "steps": [],
    "status": "starting"
}
while True:
    goal = input("\nEnter your goal (or type exit): ")

    if goal.strip() == "exit":
        break

    agent_state["goal"] = goal
    agent_state["steps"] = []
    agent_state["status"] = "starting"

    number = extract_number(goal)

    if number is None:
        print("\nCould not find a number in the goal.")
        continue

    if "prime" not in goal.lower():
        print("\nThis agent currently supports prime-number goals only.")
        continue

    if number < 2:
        print(f"\n{number} is not a prime number.")
        continue

    agent_state["steps"].append({
        "action": "analyze_goal",
        "observation": "The goal needs to be analyzed before taking an action."
    })

    agent_state["status"] = "planning"

    max_iterations = 5
    iteration = 0

    while agent_state["status"] != "completed" and iteration < max_iterations:

        iteration += 1

        print(f"\n--- Iteration {iteration} ---")

        decision_prompt = f"""
    You are an agent.

    Your goal is:
    {agent_state["goal"]}

    Current status:
    {agent_state["status"]}

    Previous steps:
    {agent_state["steps"]}

    Available actions:
    - check_divisibility
    - finish

    Rules:
    1. If the previous steps already contain enough information to answer the goal, finish the task.
    2. Do not repeat an action if its result is already available in the previous steps.
    3. Use check_divisibility only when divisibility information is needed.
    4. If the goal has been achieved, return the final answer.

    Return exactly one of:

    ACTION: check_divisibility
    DONE: <final answer>
    """

        decision = ask_agent(decision_prompt)
        decision = decision.strip()

        print("\nAgent decision:")
        print(decision)

        if "DONE:" in decision:

            agent_state["steps"].append({
                "action": decision,
                "observation": "Agent completed the goal."
            })

            agent_state["status"] = "completed"

            print("\nFinal answer:")
            print(decision)

            break

        if decision == "ACTION: check_divisibility":

            result = execute_action("check_divisibility", number)

            print("\nObservation:")
            print(result)

            agent_state["steps"].append({
                "action": decision,
                "observation": result
            })

            agent_state["status"] = "planning"

        else:

            print("\nUnknown action:", decision)

            agent_state["steps"].append({
                "action": decision,
                "observation": "Unknown action."
            })

            agent_state["status"] = "completed"

    if agent_state["status"] != "completed":
        agent_state["status"] = "stopped"
        print("\nAgent stopped: maximum iterations reached.")
    print("\nAgent state:")
    print(agent_state)