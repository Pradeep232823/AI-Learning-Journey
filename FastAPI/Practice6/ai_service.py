from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)

cache = {}

def ask_ai(text):
    
    if text in cache:
        return cache[text]
    
    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=[
            {
                "role": "user",
                "content": f"""
{text}
Answer briefly and directly.
"""
            }
        ],
        max_tokens=100
    )
    result = response.choices[0].message.content
    cache[text] = result
    return result