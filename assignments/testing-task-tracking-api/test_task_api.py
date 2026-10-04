from pathlib import Path
from runpy import run_path

import pytest
from fastapi.testclient import TestClient

starter_code = run_path(Path(__file__).with_name("starter-code.py"))
INITIAL_TASKS = starter_code["INITIAL_TASKS"]
app = starter_code["app"]
tasks = starter_code["tasks"]


@pytest.fixture
def client() -> TestClient:
    tasks.clear()
    tasks.extend(task.model_copy(deep=True) for task in INITIAL_TASKS)
    return TestClient(app)


def test_list_tasks_returns_a_list(client: TestClient) -> None:
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task_returns_the_new_task(client: TestClient) -> None:
    response = client.post(
        "/tasks",
        json={"title": "Practice testing", "description": "Write assertions"},
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Practice testing"
    assert isinstance(response.json()["id"], int)


def test_update_task_changes_the_title(client: TestClient) -> None:
    response = client.put(
        "/tasks/1",
        json={"title": "Updated title", "description": "Updated description"},
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"


def test_complete_task_sets_completed_to_true(client: TestClient) -> None:
    response = client.patch("/tasks/1/complete")

    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_task_returns_confirmation(client: TestClient) -> None:
    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert "Deleted task 1" in response.json()["message"]


def test_missing_task_returns_not_found(client: TestClient) -> None:
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_empty_title_returns_validation_error(client: TestClient) -> None:
    response = client.post("/tasks", json={"title": "", "description": "Invalid"})

    assert response.status_code == 422
    assert response.json()["detail"]


def test_missing_title_returns_validation_error(client: TestClient) -> None:
    response = client.post("/tasks", json={"description": "No title"})

    assert response.status_code == 422
    assert response.json()["detail"]


def test_unknown_task_cannot_be_updated(client: TestClient) -> None:
    response = client.put(
        "/tasks/999",
        json={"title": "Unknown", "description": "Should fail"},
    )

    assert response.status_code == 404
