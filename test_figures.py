import pytest
from figures import Bishop, King, Knight, Pawn, Queen, Rook


def test_bishop_list_available_moves_invalid_current_field():
    with pytest.raises(ValueError):
        bishop = Bishop("Z9")
        bishop.list_available_moves()


def test_bishop_list_available_moves_valid_current_field():
    bishop = Bishop("D4")
    assert len(bishop.list_available_moves()) == 13


def test_bishop_validate_move_invalid_current_field():
    with pytest.raises(ValueError):
        bishop = Bishop("A9")
        bishop.validate_move("A7")


def test_bishop_validate_move_invalid_dest_field():
    with pytest.raises(ValueError):
        bishop = Bishop("A5")
        bishop.validate_move("A9")


def test_bishop_validate_move_valid_fields_not_permitted():
    bishop = Bishop("B2")
    assert bishop.validate_move("E6") is False


def test_bishop_validate_move_valid_fields_permitted():
    bishop = Bishop("B2")
    assert bishop.validate_move("E5") is True
