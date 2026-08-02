from .conftest import (
    client,
    register_user,
    login_user,
)


def test_login_success():
    payload = register_user(client)

    token = login_user(client, payload)

    assert token is not None
    assert isinstance(token, str)


def test_login_invalid_password():
    payload = register_user(client)

    response = client.post(
        "/api/v1/users/login",
        data={
            "username": payload["username"],
            "password": "WrongPassword123",
        },
    )

    assert response.status_code == 401