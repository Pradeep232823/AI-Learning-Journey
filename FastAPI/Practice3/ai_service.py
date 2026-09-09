from openai import OpenAI
from dotenv import load_dotenv
import os
from models import StudyResult

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)

def study_topic(text):
    response = client.chat.completions.parse(
        model="gemini-flash-lite-latest",
        messages=[
            {
                "role": "user",
                "content": f"""
Explain this topic:

{text}

Return a short explanation suitable for a learner.
"""
            }
        ],
        response_format=StudyResult
    )

    return response.choices[0].message.parsed