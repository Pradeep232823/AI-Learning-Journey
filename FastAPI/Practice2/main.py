from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from ai_service import ask_ai

app = FastAPI()

class AskAI(BaseModel):
    prompt: str = Field(min_length=1)

@app.post("/ask")
def ask(request : AskAI):
    try:
        response = ask_ai(request.prompt)
        return {
            "prompt": request.prompt,
            "response": response
        }
    except Exception:
        raise HTTPException(
            status_code=500, 
            detail="AI service temporarily unavailable"
        )