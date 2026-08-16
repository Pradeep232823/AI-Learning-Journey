from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ai_service import ask_ai

app = FastAPI()

class AskRequest(BaseModel):
    prompt: str = Field(min_length=1)

class AskResponse(BaseModel):
    ai_response: str

@app.post("/ask", response_model=AskResponse)
def ask(req : AskRequest):
    try:
        response = ask_ai(req.prompt)
        return {"ai_response" : response}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="AI service temporarily unavailable"
        )