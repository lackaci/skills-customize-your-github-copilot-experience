# 📘 Assignment: Testing a Task-Tracking API

## 🎯 Objective

Write an automated test suite for a small FastAPI task-tracking application. You will practice using `pytest`, FastAPI's test client, assertions, fixtures, and tests for both successful requests and expected errors.

## 📝 Tasks

### 🛠️ Test Successful API Requests

#### Description

Use the provided API and test starter file to verify the endpoints that list, create, update, complete, and delete tasks. Each test should make a request with the test client and assert the response status code and important JSON fields.

#### Requirements

Completed program should:

- Test `GET /tasks` and confirm it returns a JSON list
- Test `POST /tasks` and confirm it creates a task with a new integer ID
- Test `PUT /tasks/{task_id}` and confirm it updates the requested task
- Test `PATCH /tasks/{task_id}/complete` and confirm the task is marked completed
- Test `DELETE /tasks/{task_id}` and confirm the response identifies the deleted task
- Use clear test names and at least one assertion in every test

### 🛠️ Test Validation and Error Cases

#### Description

Add tests for requests that should fail. Check that the API communicates errors through appropriate HTTP status codes and response data instead of silently accepting invalid input.

#### Requirements

Completed program should:

- Confirm `GET /tasks/999` returns `404`
- Confirm updating, completing, or deleting an unknown task returns `404`
- Confirm creating a task with an empty title returns `422`
- Confirm the response body contains useful error information for validation failures
- Test at least one request with invalid data types or missing required data

### 🛠️ Isolate Tests with a Fixture

#### Description

Create a `pytest` fixture that provides a fresh test client and resets the in-memory task data before each test. Run the complete suite repeatedly to demonstrate that one test does not depend on another test's changes.

#### Requirements

Completed program should:

- Define and use a fixture for the test client
- Restore the initial tasks before each test
- Pass when run with `pytest`
- Include at least eight meaningful tests
- Avoid relying on the order in which tests are collected
