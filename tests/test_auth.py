from .conftest import client
import uuid


def test_login_success():
    unique = uuid.uuid4().hex[:8]

    payload = {
        "username": f"user_{unique}",
        "email": f"{unique}@example.com",
        "password": "StrongPassword123",
    }

    register_response = client.post(
        "/api/v1/users/register",
        json=payload,
    )

    assert register_response.status_code == 200

    login_response = client.post(
        "/api/v1/users/login",
        data={
            "username": payload["username"],
            "password": payload["password"],
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()

    assert "access_token" in token
    assert token["token_type"] == "bearer"


def test_login_invalid_password():
    unique = uuid.uuid4().hex[:8]

    payload = {
        "username": f"user_{unique}",
        "email": f"{unique}@example.com",
        "password": "StrongPassword123",
    }

    client.post(
        "/api/v1/users/register",
        json=payload,
    )

    response = client.post(
        "/api/v1/users/login",
        data={
            "username": payload["username"],
            "password": "WrongPassword123",
        },
    )

    assert response.status_code == 401