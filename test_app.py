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


def test_get_list_available_moves_valid_knight(client):
    response = client.get("/api/v1/knight/d4")
    data = response.json
    assert "B3" in data["availableMoves"]
    assert "B5" in data["availableMoves"]
    assert "C2" in data["availableMoves"]
    assert "C6" in data["availableMoves"]
    assert "E2" in data["availableMoves"]
    assert "E6" in data["availableMoves"]
    assert "F3" in data["availableMoves"]
    assert "F5" in data["availableMoves"]
    assert 8 == len(data["availableMoves"])
    assert "knight" in data["figure"]
    assert response.status_code == 200


def test_get_list_available_moves_valid_pawn_first_row(client):
    response = client.get("/api/v1/pawn/e1")
    data = response.json
    assert [] == data["availableMoves"]["forBlacks"]
    assert [] == data["availableMoves"]["forWhites"]
    assert "invalid field for figure" in data["error"]["forWhites"]
    assert None is data["error"]["forBlacks"]
    assert response.status_code == 200


def test_get_list_available_moves_valid_pawn_second_row(client):
    response = client.get("/api/v1/pawn/a2")
    data = response.json
    assert "A1" in data["availableMoves"]["forBlacks"]
    assert "A3" in data["availableMoves"]["forWhites"]
    assert "A4" in data["availableMoves"]["forWhites"]
    assert None is data["error"]["forWhites"]
    assert None is data["error"]["forBlacks"]
    assert "pawn" in data["figure"]
    assert response.status_code == 200



