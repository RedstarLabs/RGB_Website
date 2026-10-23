from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from rgb_website.database.base import Base
from rgb_website.database.session import get_db
from rgb_website.main import create_app


@pytest.fixture
def client() -> Generator[TestClient]:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    app = create_app()

    def override_get_db():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    Base.metadata.drop_all(engine)
    engine.dispose()


def test_start_persists_ten_distinct_colors_and_stable_order(
    client: TestClient,
) -> None:
    started = client.post("/api/experiments")
    assert started.status_code == 201
    initial = started.json()
    session_id = initial["session_id"]

    assert initial["status"] == "in_progress"
    assert initial["answered_count"] == 0
    assert initial["next_color"]["position"] == 1
    assert len({initial["next_color"]["id"]}) == 1

    first_state = client.get(f"/api/experiments/{session_id}").json()
    assert first_state["next_color"] == initial["next_color"]

    seen_ids = []
    for trial_number in range(1, 11):
        state = client.get(f"/api/experiments/{session_id}").json()
        color = state["next_color"]
        seen_ids.append(color["id"])
        response = client.post(
            f"/api/experiments/{session_id}/responses",
            json={
                "color_id": color["id"],
                "emotion": "Freude",
                "trial_number": trial_number,
                "experiment_version": state["experiment_version"],
            },
        )
        assert response.status_code == 200
        assert response.json()["answered_count"] == trial_number

    assert len(seen_ids) == 10
    assert len(set(seen_ids)) == 10
    completed = client.get(f"/api/experiments/{session_id}").json()
    assert completed["status"] == "completed"
    assert completed["next_color"] is None


def test_state_does_not_expose_previous_answers(client: TestClient) -> None:
    session_id = client.post("/api/experiments").json()["session_id"]
    state = client.get(f"/api/experiments/{session_id}").json()
    color = state["next_color"]
    client.post(
        f"/api/experiments/{session_id}/responses",
        json={
            "color_id": color["id"],
            "emotion": "Trauer",
            "trial_number": 1,
            "experiment_version": state["experiment_version"],
        },
    )

    next_state = client.get(f"/api/experiments/{session_id}").json()
    assert "responses" not in next_state
    assert next_state["answered_count"] == 1
    assert next_state["next_color"]["id"] != color["id"]


def test_invalid_emotion_and_color_are_rejected(client: TestClient) -> None:
    session_id = client.post("/api/experiments").json()["session_id"]
    state = client.get(f"/api/experiments/{session_id}").json()
    payload = {
        "color_id": state["next_color"]["id"],
        "trial_number": 1,
        "experiment_version": state["experiment_version"],
    }
    assert (
        client.post(
            f"/api/experiments/{session_id}/responses",
            json={**payload, "emotion": "Nicht erlaubt"},
        ).status_code
        == 422
    )
    assert (
        client.post(
            f"/api/experiments/{session_id}/responses",
            json={**payload, "color_id": "unknown", "emotion": "Freude"},
        ).status_code
        == 409
    )


def test_duplicate_unknown_and_completed_requests_are_rejected(
    client: TestClient,
) -> None:
    session_id = client.post("/api/experiments").json()["session_id"]
    state = client.get(f"/api/experiments/{session_id}").json()
    payload = {
        "color_id": state["next_color"]["id"],
        "emotion": "Freude",
        "trial_number": 1,
        "experiment_version": state["experiment_version"],
    }
    endpoint = f"/api/experiments/{session_id}/responses"
    assert client.post(endpoint, json=payload).status_code == 200
    assert client.post(endpoint, json=payload).status_code == 409
    assert client.get("/api/experiments/unknown").status_code == 404

    for trial_number in range(2, 11):
        state = client.get(f"/api/experiments/{session_id}").json()
        client.post(
            endpoint,
            json={
                "color_id": state["next_color"]["id"],
                "emotion": "Freude",
                "trial_number": trial_number,
                "experiment_version": state["experiment_version"],
            },
        )
    assert client.post(endpoint, json=payload).status_code == 409


def test_invalid_trial_request_returns_conflict(client: TestClient) -> None:
    session_id = client.post("/api/experiments").json()["session_id"]
    state = client.get(f"/api/experiments/{session_id}").json()
    response = client.post(
        f"/api/experiments/{session_id}/responses",
        json={
            "color_id": state["next_color"]["id"],
            "emotion": "Freude",
            "trial_number": 2,
            "experiment_version": state["experiment_version"],
        },
    )
    assert response.status_code == 409
