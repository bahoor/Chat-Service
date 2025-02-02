# app/tests/test_routes.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_send_message(client):
    payload = {"sender": "user1", "content": "Hello, world!"}
    response = client.post("/message", json=payload)
    assert response.status_code == 200
    assert response.json()["sender"] == "user1"
    assert response.json()["content"] == "Hello, world!"

def test_get_messages(client):
    response = client.get("/message")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_message_by_id(client):
    payload = {"sender": "user2", "content": "Testing message"}
    create_response = client.post("/message", json=payload)
    message_id = create_response.json().get("_id")

    response = client.get(f"/message/{message_id}")
    assert response.status_code == 200
    assert response.json()["content"] == "Testing message"

def test_get_nonexistent_message(client):
    response = client.get("/message/655d5cbf719a507c5f0e0000")
    assert response.status_code == 404
