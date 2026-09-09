from pydantic import BaseModel, Field

class StudyRequest(BaseModel):
    topic: str = Field(min_length=1)


class StudyResponse(BaseModel):
    topic: str
    summary: str
    difficulty: str
    key_points: list[str]

class StudyResult(BaseModel):
    type: str
    data: dict