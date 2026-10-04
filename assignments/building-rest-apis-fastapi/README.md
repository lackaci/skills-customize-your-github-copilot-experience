# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that manages a collection of tasks. You will practice defining Pydantic models, creating CRUD endpoints, validating request data, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Read Tasks with GET Endpoints

#### Description

Use the starter code to implement endpoints that let a client view all tasks or retrieve one task by its ID. Each task should include an `id`, `title`, `description`, and `completed` field.

#### Requirements

Completed program should:

- Start a FastAPI application that can be run with `uvicorn`
- Return all tasks from `GET /tasks` as JSON
- Return one matching task from `GET /tasks/{task_id}`
- Return a `404 Not Found` response when the requested task ID does not exist

### 🛠️ Create and Update Tasks

#### Description

Add endpoints that allow clients to create a new task and update an existing task. Use Pydantic request models to validate incoming JSON instead of reading unstructured request data.

#### Requirements

Completed program should:

- Accept a task title and description with `POST /tasks`
- Assign a unique integer ID and set new tasks to `completed: false`
- Return a `201 Created` response when a task is added successfully
- Update an existing task with `PUT /tasks/{task_id}` and return `404 Not Found` for an unknown ID
- Reject an empty title with a clear validation error

Example request:

```json
{
  "title": "Practice FastAPI",
  "description": "Create and test the task endpoints"
}
```

### 🛠️ Complete and Delete Tasks

#### Description

Finish the API by adding an endpoint to mark a task as complete and an endpoint to delete a task. Use FastAPI’s automatic interactive documentation to try each route and check the response codes.

#### Requirements

Completed program should:

- Mark a task as complete with `PATCH /tasks/{task_id}/complete`
- Delete a task with `DELETE /tasks/{task_id}`
- Return `404 Not Found` when either endpoint receives an unknown task ID
- Return a useful success response after completing or deleting a task
- Demonstrate at least three endpoints in the interactive `/docs` page
