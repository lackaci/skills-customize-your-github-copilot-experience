from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task Tracker API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: list[Task] = [
    Task(
        id=1,
        title="Learn FastAPI",
        description="Build the first REST endpoint",
    ),
    Task(
        id=2,
        title="Test an API",
        description="Use the interactive API docs",
    ),
]


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Task Tracker API"}


@app.get("/tasks")
def read_tasks() -> list[Task]:
    # TODO: Return all tasks.
    return []


@app.get("/tasks/{task_id}")
def read_task(task_id: int) -> Task:
    # TODO: Find and return one task, or raise a 404 error.
    raise NotImplementedError


@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate) -> Task:
    # TODO: Create an ID, add the task to the list, and return it.
    raise NotImplementedError


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskCreate) -> Task:
    # TODO: Replace an existing task while preserving its ID and completion state.
    raise NotImplementedError


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int) -> Task:
    # TODO: Mark an existing task as completed and return it.
    raise NotImplementedError


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    # TODO: Remove an existing task and return a confirmation message.
    raise NotImplementedError
