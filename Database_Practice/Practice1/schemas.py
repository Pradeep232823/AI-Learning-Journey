from pydantic import BaseModel, Field, ConfigDict


class StudentCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=1)
    department: str = Field(min_length=1)


class StudentResponse(BaseModel):
    student_id: int
    name: str
    department: str