from .conftest import (
    client,
    register_user,
    login_user,
)


def test_notes_crud_workflow():
    payload = register_user(client)

    token = login_user(client, payload)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Create Note

    create_response = client.post(
        "/api/v1/notes",
        headers=headers,
        json={
            "title": "First Note",
            "content": "Testing Atlas",
        },
    )

    assert create_response.status_code == 200

    note = create_response.json()

    note_id = note["id"]

    assert note["title"] == "First Note"

    # Get Note

    get_response = client.get(
        f"/api/v1/notes/{note_id}",
        headers=headers,
    )

    assert get_response.status_code == 200

    fetched = get_response.json()

    assert fetched["id"] == note_id
    assert fetched["title"] == "First Note"
    assert fetched["content"] == "Testing Atlas"

    # Update Note

    update_response = client.put(
        f"/api/v1/notes/{note_id}",
        headers=headers,
        json={
            "title": "Updated Note",
            "content": "Updated Content",
        },
    )

    assert update_response.status_code == 200

    updated = update_response.json()

    assert updated["title"] == "Updated Note"
    assert updated["content"] == "Updated Content"

    # Delete Note

    delete_response = client.delete(
        f"/api/v1/notes/{note_id}",
        headers=headers,
    )

    assert delete_response.status_code == 200

    # Verify Deletion

    verify_response = client.get(
        f"/api/v1/notes/{note_id}",
        headers=headers,
    )

    assert verify_response.status_code == 404