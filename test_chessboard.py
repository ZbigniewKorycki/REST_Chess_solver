from chessboard import Chessboard


def test_get_fields_of_chessboard():
    fields = Chessboard.get_fields_of_chessboard()
    assert len(fields) == 64
    assert "A1" in fields
    assert "H8" in fields


def test_check_if_field_in_chessboard():
    assert Chessboard.check_if_field_in_chessboard("A1") is True
    assert Chessboard.check_if_field_in_chessboard("H8") is True
    assert Chessboard.check_if_field_in_chessboard("C4") is True
    assert Chessboard.check_if_field_in_chessboard("H10") is False
    assert Chessboard.check_if_field_in_chessboard("Z9") is False


def test_change_column():
    assert Chessboard.change_column("A", 1) == "B"
    assert Chessboard.change_column("H", 3) == "K"
    assert Chessboard.change_column("H", -1) == "G"


def test_change_row():
    assert Chessboard.change_row(1, 1) == 2
    assert Chessboard.change_row(8, 3) == 11
    assert Chessboard.change_row(8, -1) == 7
    assert Chessboard.change_row(8, -3) == 5


def test_get_col_and_row_from_field():
    assert Chessboard.get_col_and_row_from_field("E4") == ("E", 4)
    assert Chessboard.get_col_and_row_from_field("H8") == ("H", 8)
    assert Chessboard.get_col_and_row_from_field("c9") == ("C", 9)


def test_get_field_from_col_and_row():
    assert Chessboard.get_field_from_col_and_row("B", 3) == "B3"
    assert Chessboard.get_field_from_col_and_row("G", 6) == "G6"
    assert Chessboard.get_field_from_col_and_row("Z", 21) == "Z21"
