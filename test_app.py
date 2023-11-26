import pytest
from app import app


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_get_list_available_moves_invalid_figure(client):
    response = client.get("/api/v1/non_existing_figure/a4")
    data = response.json
    assert "invalid figure" in data["error"]
    assert "a4" in data["currentField"]
    assert [] == data["availableMoves"]
    assert response.status_code == 404


def test_get_list_available_moves_invalid_field(client):
    response = client.get("/api/v1/pawn/a9")
    data = response.json
    assert "current field does not exist" in data["error"]
    assert [] == data["availableMoves"]
    assert response.status_code == 409
