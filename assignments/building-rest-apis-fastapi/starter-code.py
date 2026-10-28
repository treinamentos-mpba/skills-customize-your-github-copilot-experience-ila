from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


tasks = {}
next_task_id = 1

# Add the API routes below.