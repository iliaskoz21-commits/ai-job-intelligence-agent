from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_project_information():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "AI Job Intelligence Agent is running",
        "version": "0.1.0",
    }


def test_health_check_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
