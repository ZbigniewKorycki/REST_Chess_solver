from figure import Figure
from chessboard import Chessboard


class Pawn(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)
        self.chessboard = Chessboard()

    def list_available_moves(self):
        available_moves = {"blacks": [], "whites": []}
        if self.current_field not in self.chessboard.fields:
            return available_moves

        direction_for_whites = Chessboard.get_field_after_moving_up
        direction_for_blacks = Chessboard.get_field_after_moving_down
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            self.current_field
        )

        if current_row == 2:
            for distance_to_possible_field_for_whites in range(1, 3):
                possible_field_for_white = direction_for_whites(
                    self.current_field, distance_to_possible_field_for_whites
                )
                if possible_field_for_white in self.chessboard.fields:
                    available_moves["whites"].append(possible_field_for_white)

            possible_field_for_black = direction_for_blacks(self.current_field, 1)
            if possible_field_for_black in self.chessboard.fields:
                available_moves["blacks"].append(possible_field_for_black)

        if current_row == 7:
            possible_field_for_white = direction_for_whites(self.current_field, 1)
            if possible_field_for_white in self.chessboard.fields:
                available_moves["whites"].append(possible_field_for_white)

            for distance_to_possible_field_for_blacks in range(1, 3):
                possible_field_for_black = direction_for_blacks(
                    self.current_field, distance_to_possible_field_for_blacks
                )
                if possible_field_for_black in self.chessboard.fields:
                    available_moves["blacks"].append(possible_field_for_black)

        if current_row in range(3, 7):
            possible_field_for_white = direction_for_whites(self.current_field, 1)
            if possible_field_for_white in self.chessboard.fields:
                available_moves["whites"].append(possible_field_for_white)

            possible_field_for_black = direction_for_blacks(self.current_field, 1)
            if possible_field_for_black in self.chessboard.fields:
                available_moves["blacks"].append(possible_field_for_black)

        else:
            return available_moves

        return available_moves

    def validate_move(self, dest_field: str) -> str:
        if self.chessboard.check_if_field_in_chessboard(dest_field):
            if dest_field.upper() in self.list_available_moves():
                return "valid"
            else:
                return "invalid"
        else:
            return "field does not exists."
