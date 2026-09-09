from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ai_service import ask_ai

app = FastAPI()

class AskRequest(BaseModel):
    prompt: str = Field(min_length=1)


@app.post("/ask")
def ask(request: AskRequest):
    try:
        response = ask_ai(request.prompt)

        return {
            "response": response
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="AI service temporarily unavailable"
        )