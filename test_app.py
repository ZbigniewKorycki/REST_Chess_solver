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
    assert "B3" and "B5" and "C2" and "C6" and "E2" and "E6" and "F3" and "F5" in data["availableMoves"]
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
    assert "A3" and "A4" in data["availableMoves"]["forWhites"]
    assert None is data["error"]["forWhites"]
    assert None is data["error"]["forBlacks"]
    assert "pawn" in data["figure"]
    assert response.status_code == 200


def test_get_list_available_moves_valid_pawn_sixth_row(client):
    response = client.get("/api/v1/pawn/g6")
    data = response.json
    assert "G5" in data["availableMoves"]["forBlacks"]
    assert 1 == len(data["availableMoves"]["forBlacks"])
    assert "G7" in data["availableMoves"]["forWhites"]
    assert 1 == len(data["availableMoves"]["forWhites"])
    assert None is data["error"]["forWhites"]
    assert None is data["error"]["forBlacks"]
    assert response.status_code == 200


def test_get_list_available_moves_valid_pawn_seventh_row(client):
    response = client.get("/api/v1/pawn/b7")
    data = response.json
    assert "B6" and "B5" in data["availableMoves"]["forBlacks"]
    assert 2 == len(data["availableMoves"]["forBlacks"])
    assert "B8" in data["availableMoves"]["forWhites"]
    assert 1 == len(data["availableMoves"]["forWhites"])
    assert None is data["error"]["forWhites"]
    assert None is data["error"]["forBlacks"]
    assert response.status_code == 200


def test_get_list_available_moves_valid_pawn_eighth_row(client):
    response = client.get("/api/v1/pawn/c8")
    data = response.json
    assert [] == data["availableMoves"]["forBlacks"]
    assert [] == data["availableMoves"]["forWhites"]
    assert None is data["error"]["forWhites"]
    assert "invalid field for figure" in data["error"]["forBlacks"]
    assert response.status_code == 200


def test_get_list_available_moves_valid_king(client):
    response = client.get("/api/v1/king/b1")
    data = response.json
    assert "A1" and "A2" and "B2" and "C1" and "C2" in data["availableMoves"]
    assert 5 == len(data["availableMoves"])
    assert None is data["error"]
    assert "king" in data["figure"]
    assert response.status_code == 200

