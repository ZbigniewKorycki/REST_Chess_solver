class Chessboard:
    ROWS = range(1, 9)
    COLUMNS = "ABCDEFGH"

    def __init__(self, rows=ROWS, columns=COLUMNS):
        self.rows = rows
        self.columns = columns
        self.rows_size = len(rows)
        self.columns_size = len(columns)
        self.fields = self.get_fields_of_chessboard()

    def get_fields_of_chessboard(self) -> list:
        fields = [f"{column}{row}" for row in self.rows for column in self.columns]
        return fields

    def check_if_field_in_chessboard(self, field: str) -> bool:
        if field.upper() in self.fields:
            return True
        else:
            return False

    @staticmethod
    def increment_column(column: str, increment_by: int) -> str:
        char_ascii = ord(column)
        incremented_ascii = char_ascii + increment_by
        result_column = chr(incremented_ascii)
        return result_column

    @staticmethod
    def decrement_column(column: str, decrement_by: int) -> str:
        char_ascii = ord(column)
        decremented_ascii = char_ascii - decrement_by
        result_column = chr(decremented_ascii)
        return result_column

    @staticmethod
    def increment_row(row: int, increment_by: int) -> int:
        return row + increment_by

    @staticmethod
    def decrement_row(row: int, decrement_by: int) -> int:
        return row - decrement_by

    @staticmethod
    def get_column_and_row_from_field(field: str) -> tuple:
        column = field[0].upper()
        row = int(field[1])
        return column, row

    @staticmethod
    def get_field_from_column_and_row(column: str, row: int) -> str:
        return "".join([column, str(row)])

    @staticmethod
    def get_field_after_moving_diagonally_up_left(
        current_field: str, movement_by: int
    ) -> str:
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            current_field
        )
        new_column = Chessboard.increment_column(current_column, movement_by)
        new_row = Chessboard.decrement_row(current_row, movement_by)
        new_field = Chessboard.get_field_from_column_and_row(new_column, new_row)
        return new_field

    @staticmethod
    def get_field_after_moving_diagonally_up_right(
        current_field: str, movement_by: int
    ) -> str:
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            current_field
        )
        new_column = Chessboard.increment_column(current_column, movement_by)
        new_row = Chessboard.increment_row(current_row, movement_by)
        new_field = Chessboard.get_field_from_column_and_row(new_column, new_row)
        return new_field

    @staticmethod
    def get_field_after_moving_diagonally_down_left(
        current_field: str, movement_by: int
    ) -> str:
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            current_field
        )
        new_column = Chessboard.decrement_column(current_column, movement_by)
        new_row = Chessboard.decrement_row(current_row, movement_by)
        new_field = Chessboard.get_field_from_column_and_row(new_column, new_row)
        return new_field

    @staticmethod
    def get_field_after_moving_diagonally_down_right(
        current_field: str, movement_by: int
    ) -> str:
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            current_field
        )
        new_column = Chessboard.decrement_column(current_column, movement_by)
        new_row = Chessboard.increment_row(current_row, movement_by)
        new_field = Chessboard.get_field_from_column_and_row(new_column, new_row)
        return new_field

    @staticmethod
    def get_field_after_moving_up(current_field: str, movement_by: int) -> str:
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            current_field
        )
        new_row = Chessboard.increment_row(current_row, movement_by)
        new_field = Chessboard.get_field_from_column_and_row(current_column, new_row)
        return new_field

    @staticmethod
    def get_field_after_moving_down(current_field: str, movement_by: int) -> str:
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            current_field
        )
        new_row = Chessboard.decrement_row(current_row, movement_by)
        new_field = Chessboard.get_field_from_column_and_row(current_column, new_row)
        return new_field

    @staticmethod
    def get_field_after_moving_left(current_field: str, movement_by: int) -> str:
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            current_field
        )
        new_column = Chessboard.decrement_column(current_column, movement_by)
        new_field = Chessboard.get_field_from_column_and_row(new_column, current_row)
        return new_field

    @staticmethod
    def get_field_after_moving_right(current_field: str, movement_by: int) -> str:
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            current_field
        )
        new_column = Chessboard.increment_column(current_column, movement_by)
        new_field = Chessboard.get_field_from_column_and_row(new_column, current_row)
        return new_field
