from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ai_service import study_topic

app = FastAPI()

class StudyRequest(BaseModel):
    topic: str = Field(min_length=1)

@app.post("/study")
def study(request: StudyRequest):
    try:
        result = study_topic(request.topic)

        return result

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="AI service temporarily unavailable"
        )