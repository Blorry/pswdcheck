from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "broken"}


def test_check_weak():
    response = client.post("/check", json={"password": "abc"})
    assert response.status_code == 200
    assert response.json()["strength"] == "weak"


def test_check_strong():
    response = client.post("/check", json={"password": "Xk9$mP2@qLz!7Wn#"})
    assert response.json()["strength"] in ("strong", "very strong")


def test_check_missing_field():
    response = client.post("/check", json={})
    assert response.status_code == 422


def test_generate_endpoint():
    response = client.get("/generate?length=24")
    body = response.json()
    assert body["length"] == 24
    assert len(body["password"]) == 24
