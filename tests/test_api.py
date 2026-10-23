from fastapi.testclient import TestClient

from rgb_website.main import create_app


def test_health_endpoint_does_not_expose_configuration() -> None:
    response = TestClient(create_app()).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
