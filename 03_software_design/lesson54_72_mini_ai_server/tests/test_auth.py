from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_missing_api_key():
    response = client.post(
        "/chat",
        json = {
            "message": "Hello"
        }
    )
    assert response.status_code == 401

def test_invalid_api_key():
    response = client.post(
        "/chat",
        headers={
            "X-API-Key": "wrong-key"
        },
        json={
            "message": "Hello"
        }
    )
    assert response.status_code == 401

def test_valid_api_key():
    response = client.post(
            "/chat",
            headers={
                "X-API-Key": "key-alice"
            },
            json={
                "message": "Hello"
            }
        )
    assert response.status_code == 200

def test_user_cannot_access_admin():
    response = client.get(
        "/admin",
        headers = {
            "X-API-Key": "key-alice"
        }
    )
    assert response.status_code == 403

def test_admin_can_access_admin():
    response = client.get(
        "/admin",
        headers = {
            "X-API-Key": "key-bob"
        }
    )
    assert response.status_code == 200