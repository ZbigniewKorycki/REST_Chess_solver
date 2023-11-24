import string


class Chessboard:

    ROWS_SIZE = 8
    COLUMNS_SIZE = 8

    def __init__(self, rows_size=ROWS_SIZE, columns_size=COLUMNS_SIZE):
        self.row_size = rows_size
        self.columns_size = columns_size
        self.fields = self.get_fields_of_chessboard()

    def get_fields_of_chessboard(self) -> list:
        fields = [f"{column}{row}" for row in range(1, self.row_size + 1) for column in
                  string.ascii_uppercase[0:self.columns_size]]
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
