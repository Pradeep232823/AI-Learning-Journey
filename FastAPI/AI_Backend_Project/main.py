from fastapi import FastAPI, HTTPException
from models import StudyRequest, StudyResult
from ai_service import ask_ai

app = FastAPI()
@app.post("/study", response_model=StudyResult)
def study(request: StudyRequest):
    try:
        result = ask_ai(request.topic)

        return result

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="AI service temporarily unavailable"
        )