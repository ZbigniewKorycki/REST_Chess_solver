class Chessboard:
    ROWS = range(1, 9)
    COLUMNS = "ABCDEFGH"

    @classmethod
    def get_fields_of_chessboard(cls) -> list:
        fields = [f"{col}{row}" for row in cls.ROWS for col in cls.COLUMNS]
        return fields

    @staticmethod
    def check_if_field_in_chessboard(field: str) -> bool:
        if field.upper() in Chessboard.get_fields_of_chessboard():
            return True
        else:
            return False

    @staticmethod
    def change_column(column: str, change_by: int) -> str:
        char_ascii = ord(column)
        changed_ascii = char_ascii + change_by
        result_column = chr(changed_ascii)
        return result_column

    @staticmethod
    def change_row(curr_row: int, move_by: int) -> int:
        return curr_row + move_by

    @staticmethod
    def get_col_and_row_from_field(field: str) -> tuple:
        column = field[0].upper()
        row = int(field[1])
        return column, row

    @staticmethod
    def get_field_from_col_and_row(column: str, row: int) -> str:
        return "".join([column, str(row)])

    @staticmethod
    def get_field_after_move_up_left(curr_field: str, move_by: int) -> str:
        return Chessboard.get_field_after_move(curr_field, -move_by, move_by)

    @staticmethod
    def get_field_after_move_up_right(curr_field: str, move_by: int) -> str:
        return Chessboard.get_field_after_move(curr_field, move_by, move_by)

    @staticmethod
    def get_field_after_move_down_left(curr_field: str, move_by: int) -> str:
        return Chessboard.get_field_after_move(curr_field, -move_by, -move_by)

    @staticmethod
    def get_field_after_move_down_right(curr_field: str, move_by: int) -> str:
        return Chessboard.get_field_after_move(curr_field, move_by, -move_by)

    @staticmethod
    def get_field_after_move_up(curr_field: str, move_by: int) -> str:
        return Chessboard.get_field_after_move(curr_field, 0, move_by)

    @staticmethod
    def get_field_after_move_down(curr_field: str, move_by: int) -> str:
        return Chessboard.get_field_after_move(curr_field, 0, -move_by)

    @staticmethod
    def get_field_after_move_left(curr_field: str, move_by: int) -> str:
        return Chessboard.get_field_after_move(curr_field, -move_by, 0)

    @staticmethod
    def get_field_after_move_right(curr_field: str, move_by: int) -> str:
        return Chessboard.get_field_after_move(curr_field, move_by, 0)

    @staticmethod
    def get_field_after_move(
        curr_field: str, move_by_col: int, move_by_row: int
    ) -> str:
        curr_col, curr_row = Chessboard.get_col_and_row_from_field(curr_field)
        new_col = Chessboard.change_column(curr_col, move_by_col)
        new_row = Chessboard.change_row(curr_row, move_by_row)
        new_field = Chessboard.get_field_from_col_and_row(new_col, new_row)
        return new_field
