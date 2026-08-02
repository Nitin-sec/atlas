from .conftest import client

def test_health_endpoint():
    response = client.get("/api/v1/health")

    assert response.status_code == 200