from figure import Figure
from chessboard import Chessboard


class Knight(Figure):

    def __init__(self, current_field: str):
        super().__init__(current_field)
        self.chessboard = Chessboard()
        self.available_moves = self.list_available_moves()

    def list_available_moves(self) -> list:
        available_moves = []
        if self.current_field in self.chessboard.fields:
            directions_combinations = [
                [Chessboard.get_field_after_moving_up, Chessboard.get_field_after_moving_right],
                [Chessboard.get_field_after_moving_up, Chessboard.get_field_after_moving_left],
                [Chessboard.get_field_after_moving_down, Chessboard.get_field_after_moving_right],
                [Chessboard.get_field_after_moving_down, Chessboard.get_field_after_moving_left],
                [Chessboard.get_field_after_moving_left, Chessboard.get_field_after_moving_up],
                [Chessboard.get_field_after_moving_left, Chessboard.get_field_after_moving_down],
                [Chessboard.get_field_after_moving_right, Chessboard.get_field_after_moving_up],
                [Chessboard.get_field_after_moving_right, Chessboard.get_field_after_moving_down]
            ]
            for direction in directions_combinations:
                distance_to_intermediate = 2
                intermediate_field = direction[0](self.current_field, distance_to_intermediate)
                distance = 1
                new_field = direction[1](intermediate_field, distance)
                if new_field in self.chessboard.fields:
                    available_moves.append(new_field)
        else:
            return []
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> str:
        if self.chessboard.check_if_field_in_chessboard(dest_field):
            if dest_field.upper() in self.available_moves:
                return "Field available"
            else:
                return "Field not available."
        else:
            return "Field does not exists."
