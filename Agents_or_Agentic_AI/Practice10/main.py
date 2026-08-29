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


def ask_agent(role, task):
    prompt = f"""
You are a {role}.

Task:
{task}

Return a short response.
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

def apply_guardrail(response):

    blocked_words = ["password", "secret", "api_key"]

    for word in blocked_words:
        if word.lower() in response.lower():
            return {
                "allowed": False,
                "reason": f"Response contains blocked content: {word}"
            }

    return {
        "allowed": True,
        "reason": ""
    }


researcher_result = ask_agent(
    "research agent",
    "Explain what RAG is."
)
reviewer_result = ask_agent(
    "reviewer agent",
    f"""
Review the following research response:

{researcher_result}

Check whether it is accurate, relevant, and concise.
"""
)

research_guard = apply_guardrail(researcher_result)
review_guard = apply_guardrail(reviewer_result)

print("\nResearcher:")
print(researcher_result)

print("\nResearch Guardrail:")
print(research_guard)

print("\nReviewer:")
print(reviewer_result)

print("\nReview Guardrail:")
print(review_guard)