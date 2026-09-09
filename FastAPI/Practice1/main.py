from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/response")
def get_response():
    return {
        "message" : "Task FastAPI is running."
    }

@app.get("/task/{task_id}")
def get_task(task_id : int):
    return {
        "task_id" : task_id,
        "message" : f"Task {task_id} requested."
    }

@app.get("/tasks")
def get_tasks(limit: int):
    return {"limit": limit}

class TaskRequest(BaseModel):
    title: str = Field(min_length=1)
    priority: int = Field(ge=1, le=5)

@app.post("/tasks/")
def add_task(task_request : TaskRequest):
    if task_request.priority == 5:
        raise HTTPException(status_code=400, detail="High priority tasks require confirmation.")
    return {
        "title": task_request.title,
        "priority": task_request.priority
    }