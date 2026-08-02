from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

import uuid


def create_user_payload():
    unique = uuid.uuid4().hex[:8]

    return {
        "username": f"user_{unique}",
        "email": f"{unique}@example.com",
        "password": "StrongPassword123",
    }


def register_user(client):
    payload = create_user_payload()

    response = client.post(
        "/api/v1/users/register",
        json=payload,
    )

    assert response.status_code == 200

    return payload


def login_user(client, payload):
    response = client.post(
        "/api/v1/users/login",
        data={
            "username": payload["username"],
            "password": payload["password"],
        },
    )

    assert response.status_code == 200

    return response.json()["access_token"]