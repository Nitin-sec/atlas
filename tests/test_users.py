from .conftest import client
import uuid


def test_create_user():
    unique = uuid.uuid4().hex[:8]

    payload = {
        "username": f"user_{unique}",
        "email": f"{unique}@example.com",
        "password": "StrongPassword123"
    }

    response = client.post(
        "/api/v1/users/register",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]