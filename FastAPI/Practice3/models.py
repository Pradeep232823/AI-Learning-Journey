from pydantic import BaseModel

class StudyResult(BaseModel):
    topic: str
    summary: str
    difficulty: str