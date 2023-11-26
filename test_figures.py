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


def test_rook_list_available_moves_invalid_current_field():
    with pytest.raises(ValueError):
        rook = Rook("B10")
        rook.list_available_moves()


def test_rook_list_available_moves_valid_current_field():
    rook = Rook("C1")
    assert len(rook.list_available_moves()) == 14


def test_rook_validate_move_invalid_current_field():
    with pytest.raises(ValueError):
        rook = Rook("A9")
        rook.validate_move("A7")


def test_rook_validate_move_invalid_dest_field():
    with pytest.raises(ValueError):
        rook = Rook("A5")
        rook.validate_move("A9")


def test_rook_validate_move_valid_fields_not_permitted():
    rook = Rook("B2")
    assert rook.validate_move("E6") is False


def test_rook_validate_move_valid_fields_permitted():
    rook = Rook("B2")
    assert rook.validate_move("B5") is True


def test_knight_list_available_moves_invalid_current_field():
    with pytest.raises(ValueError):
        knight = Knight("B10")
        knight.list_available_moves()


def test_knight_list_available_moves_valid_current_field():
    knight = Knight("D4")
    assert len(knight.list_available_moves()) == 8


def test_knight_validate_move_invalid_current_field():
    with pytest.raises(ValueError):
        knight = Knight("A9")
        knight.validate_move("A7")


def test_knight_validate_move_invalid_dest_field():
    with pytest.raises(ValueError):
        knight = Knight("A5")
        knight.validate_move("A9")


def test_knight_validate_move_valid_fields_not_permitted():
    knight = Knight("B2")
    assert knight.validate_move("E6") is False


def test_knight_validate_move_valid_fields_permitted():
    knight = Knight("B2")
    assert knight.validate_move("C4") is True


def test_king_list_available_moves_invalid_current_field():
    with pytest.raises(ValueError):
        king = King("B10")
        king.list_available_moves()


def test_king_list_available_moves_valid_current_field():
    king = King("A1")
    assert len(king.list_available_moves()) == 3


def test_king_validate_move_invalid_current_field():
    with pytest.raises(ValueError):
        king = King("A9")
        king.validate_move("A7")


def test_king_validate_move_invalid_dest_field():
    with pytest.raises(ValueError):
        king = King("A5")
        king.validate_move("A9")


def test_king_validate_move_valid_fields_not_permitted():
    king = King("B2")
    assert king.validate_move("E6") is False


def test_king_validate_move_valid_fields_permitted():
    king = King("C2")
    assert king.validate_move("C3") is True


def test_queen_list_available_moves_invalid_current_field():
    with pytest.raises(ValueError):
        queen = Queen("C11")
        queen.list_available_moves()


def test_queen_list_available_moves_valid_current_field():
    queen = Queen("E3")
    assert len(queen.list_available_moves()) == 25


def test_queen_validate_move_invalid_current_field():
    with pytest.raises(ValueError):
        queen = Queen("A9")
        queen.validate_move("A7")


def test_queen_validate_move_invalid_dest_field():
    with pytest.raises(ValueError):
        queen = Queen("A5")
        queen.validate_move("A9")


def test_queen_validate_move_valid_fields_not_permitted():
    queen = Queen("C2")
    assert queen.validate_move("D8") is False


def test_queen_validate_move_valid_fields_permitted():
    queen = Queen("C2")
    assert queen.validate_move("C8") is True


def test_pawn_list_available_moves_invalid_current_field():
    with pytest.raises(ValueError):
        pawn = Pawn("C11")
        pawn.list_available_moves()


def test_pawn_list_available_moves_valid_current_field():
    pawn = Pawn("B2")
    assert len(pawn.list_available_moves()[0]["whites"]) == 2
    assert len(pawn.list_available_moves()[0]["blacks"]) == 1


def test_pawn_validate_move_invalid_current_field():
    with pytest.raises(ValueError):
        pawn = Pawn("A9")
        pawn.validate_move("A7")


def test_pawn_validate_move_invalid_dest_field():
    with pytest.raises(ValueError):
        pawn = Pawn("A5")
        pawn.validate_move("A9")


def test_pawn_validate_move_valid_fields_both_color_not_permitted():
    pawn = Pawn("C2")
    result = pawn.validate_move("D8")
    assert result.white is False
    assert result.black is False


def test_pawn_validate_move_valid_fields_whites_only_permitted():
    pawn = Pawn("C2")
    result = pawn.validate_move("C3")
    assert result.white is True
    assert result.black is False


def test_pawn_validate_move_valid_fields_blacks_only_permitted():
    pawn = Pawn("C6")
    result = pawn.validate_move("C5")
    assert result.white is False
    assert result.black is True


def test_pawn_validate_move_valid_fields_row_first():
    pawn = Pawn("E1")
    result = pawn.validate_move("E3")
    assert result.white is None
    assert result.black is False


def test_pawn_validate_move_valid_fields_eight_first():
    pawn = Pawn("H8")
    result = pawn.validate_move("H6")
    assert result.white is False
    assert result.black is None
