from copy import deepcopy

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Task Tracker API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""


class Task(TaskCreate):
    id: int
    completed: bool = False


INITIAL_TASKS = [
    Task(
        id=1,
        title="Learn FastAPI",
        description="Build the first REST endpoint",
    ),
    Task(
        id=2,
        title="Write tests",
        description="Verify API behavior automatically",
    ),
]
tasks: list[Task] = deepcopy(INITIAL_TASKS)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Task Tracker API"}


@app.get("/tasks")
def read_tasks() -> list[Task]:
    return tasks


@app.get("/tasks/{task_id}")
def read_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate) -> Task:
    next_id = max((task.id for task in tasks), default=0) + 1
    task = Task(id=next_id, **task_data.model_dump())
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskCreate) -> Task:
    task = read_task(task_id)
    task.title = task_data.title
    task.description = task_data.description
    return task


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int) -> Task:
    task = read_task(task_id)
    task.completed = True
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    task = read_task(task_id)
    tasks.remove(task)
    return {"message": f"Deleted task {task.id}"}
