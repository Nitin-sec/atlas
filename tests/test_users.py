from .conftest import client, create_user_payload


def test_create_user():
    payload = create_user_payload()

    response = client.post(
        "/api/v1/users/register",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]

def test_duplicate_user_registration():
    payload = create_user_payload()

    first_response = client.post(
        "/api/v1/users/register",
        json=payload,
    )

    assert first_response.status_code == 200

    second_response = client.post(
        "/api/v1/users/register",
        json=payload,
    )

    assert second_response.status_code == 409

    print(second_response.json())