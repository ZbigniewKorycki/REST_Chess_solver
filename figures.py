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
                    possible_field = direction(
                        self.current_field, distance_to_possible_field
                    )
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
                return "valid"
            else:
                return "invalid"
        else:
            return "field does not exists."


class King(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)
        self.chessboard = Chessboard()

    def list_available_moves(self) -> list:
        available_moves = []
        if self.current_field in self.chessboard.fields:
            directions = [
                Chessboard.get_field_after_moving_up,
                Chessboard.get_field_after_moving_down,
                Chessboard.get_field_after_moving_left,
                Chessboard.get_field_after_moving_right,
                Chessboard.get_field_after_moving_diagonally_up_left,
                Chessboard.get_field_after_moving_diagonally_up_right,
                Chessboard.get_field_after_moving_diagonally_down_left,
                Chessboard.get_field_after_moving_diagonally_down_right,
            ]
            for direction in directions:
                distance_to_possible_field = 1
                possible_field = direction(
                    self.current_field, distance_to_possible_field
                )
                if possible_field in self.chessboard.fields:
                    available_moves.append(possible_field)
        else:
            return []
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> str:
        if self.chessboard.check_if_field_in_chessboard(dest_field):
            if dest_field.upper() in self.list_available_moves():
                return "valid"
            else:
                return "invalid"
        else:
            return "field does not exists."


class Knight(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)
        self.chessboard = Chessboard()

    def list_available_moves(self) -> list:
        available_moves = []
        if self.current_field in self.chessboard.fields:
            directions_combinations = [
                [
                    Chessboard.get_field_after_moving_up,
                    Chessboard.get_field_after_moving_right,
                ],
                [
                    Chessboard.get_field_after_moving_up,
                    Chessboard.get_field_after_moving_left,
                ],
                [
                    Chessboard.get_field_after_moving_down,
                    Chessboard.get_field_after_moving_right,
                ],
                [
                    Chessboard.get_field_after_moving_down,
                    Chessboard.get_field_after_moving_left,
                ],
                [
                    Chessboard.get_field_after_moving_left,
                    Chessboard.get_field_after_moving_up,
                ],
                [
                    Chessboard.get_field_after_moving_left,
                    Chessboard.get_field_after_moving_down,
                ],
                [
                    Chessboard.get_field_after_moving_right,
                    Chessboard.get_field_after_moving_up,
                ],
                [
                    Chessboard.get_field_after_moving_right,
                    Chessboard.get_field_after_moving_down,
                ],
            ]
            for direction in directions_combinations:
                distance_to_intermediate_field = 2
                distance_to_possible_field = 1
                possible_field = direction[1](
                    direction[0](self.current_field, distance_to_intermediate_field),
                    distance_to_possible_field,
                )
                if possible_field in self.chessboard.fields:
                    available_moves.append(possible_field)
        else:
            return []
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> str:
        if self.chessboard.check_if_field_in_chessboard(dest_field):
            if dest_field.upper() in self.list_available_moves():
                return "valid"
            else:
                return "invalid"
        else:
            return "field does not exists."


class Pawn(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)
        self.chessboard = Chessboard()

    def list_available_moves(self) -> list:
        available_moves = [{"blacks": [], "whites": []}]
        if self.current_field not in self.chessboard.fields:
            return []

        direction_for_whites = Chessboard.get_field_after_moving_up
        direction_for_blacks = Chessboard.get_field_after_moving_down
        current_column, current_row = Chessboard.get_column_and_row_from_field(
            self.current_field
        )

        if current_row == 2:
            for distance_to_possible_field_for_whites in [1, 2]:
                possible_field_for_white = direction_for_whites(
                    self.current_field, distance_to_possible_field_for_whites
                )
                if possible_field_for_white in self.chessboard.fields:
                    available_moves[0]["whites"].append(possible_field_for_white)

            possible_field_for_black = direction_for_blacks(self.current_field, 1)
            if possible_field_for_black in self.chessboard.fields:
                available_moves[0]["blacks"].append(possible_field_for_black)

        if current_row == 7:
            possible_field_for_white = direction_for_whites(self.current_field, 1)
            if possible_field_for_white in self.chessboard.fields:
                available_moves[0]["whites"].append(possible_field_for_white)

            for distance_to_possible_field_for_blacks in [1, 2]:
                possible_field_for_black = direction_for_blacks(
                    self.current_field, distance_to_possible_field_for_blacks
                )
                if possible_field_for_black in self.chessboard.fields:
                    available_moves[0]["blacks"].append(possible_field_for_black)

        if current_row in range(3, 7):
            possible_field_for_white = direction_for_whites(self.current_field, 1)
            if possible_field_for_white in self.chessboard.fields:
                available_moves[0]["whites"].append(possible_field_for_white)

            possible_field_for_black = direction_for_blacks(self.current_field, 1)
            if possible_field_for_black in self.chessboard.fields:
                available_moves[0]["blacks"].append(possible_field_for_black)

        if current_row == 1:
            return [{"blacks": []}]
        if current_row == 8:
            return [{"whites": []}]
        return available_moves

    def validate_move(self, dest_field: str) -> str:
        if self.chessboard.check_if_field_in_chessboard(dest_field):
            if dest_field.upper() in self.list_available_moves():
                return "valid"
            else:
                return "invalid"
        else:
            return "field does not exists."


class Queen(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)
        self.chessboard = Chessboard()

    def list_available_moves(self) -> list:
        available_moves = []
        if self.current_field in self.chessboard.fields:
            directions = [
                Chessboard.get_field_after_moving_up,
                Chessboard.get_field_after_moving_down,
                Chessboard.get_field_after_moving_left,
                Chessboard.get_field_after_moving_right,
                Chessboard.get_field_after_moving_diagonally_up_left,
                Chessboard.get_field_after_moving_diagonally_up_right,
                Chessboard.get_field_after_moving_diagonally_down_left,
                Chessboard.get_field_after_moving_diagonally_down_right,
            ]
            for direction in directions:
                for distance_to_possible_field in range(1, 8):
                    possible_field = direction(
                        self.current_field, distance_to_possible_field
                    )
                    if possible_field in self.chessboard.fields:
                        available_moves.append(possible_field)
                    else:
                        break
        else:
            return []
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> str:
        if self.chessboard.check_if_field_in_chessboard(dest_field):
            if dest_field.upper() in self.list_available_moves():
                return "valid"
            else:
                return "invalid"
        else:
            return "field does not exists."


class Rook(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)
        self.chessboard = Chessboard()

    def list_available_moves(self) -> list:
        available_moves = []
        if self.current_field in self.chessboard.fields:
            directions = [
                Chessboard.get_field_after_moving_up,
                Chessboard.get_field_after_moving_down,
                Chessboard.get_field_after_moving_left,
                Chessboard.get_field_after_moving_right,
            ]
            for direction in directions:
                for distance_to_possible_field in range(1, 8):
                    possible_field = direction(
                        self.current_field, distance_to_possible_field
                    )
                    if possible_field in self.chessboard.fields:
                        available_moves.append(possible_field)
                    else:
                        break
        else:
            return []
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> str:
        if self.chessboard.check_if_field_in_chessboard(dest_field):
            if dest_field.upper() in self.list_available_moves():
                return "valid"
            else:
                return "invalid"
        else:
            return "field does not exists."
