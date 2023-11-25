from figure import Figure
from chessboard import Chessboard


class Bishop(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)
        self.chessboard = Chessboard()

    def list_available_moves(self) -> list:
        available_moves = []
        if self.current_field in self.chessboard.fields:
            directions = [
                Chessboard.get_field_after_moving_diagonally_up_left,
                Chessboard.get_field_after_moving_diagonally_up_right,
                Chessboard.get_field_after_moving_diagonally_down_left,
                Chessboard.get_field_after_moving_diagonally_down_right,
            ]
            for direction in directions:
                for distance_to_possible_field in range(1, 8):
                    possible_field = direction(self.current_field, distance_to_possible_field)
                    if possible_field in self.chessboard.fields:
                        available_moves.append(possible_field)
                    else:
                        break
        else:
            return []
        return sorted(available_moves)

    def validate_move(self, dest_field: str):
        if self.chessboard.check_if_field_in_chessboard(dest_field):
            if dest_field.upper() in self.list_available_moves():
                return "Field available"
            else:
                return "Field not available."
        else:
            return "Field does not exists."
