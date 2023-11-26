from figure import Figure
from chessboard import Chessboard
from collections import namedtuple


class Bishop(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)

    def list_available_moves(self) -> list:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        available_moves = []
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
                if Chessboard.check_if_field_in_chessboard(possible_field):
                    available_moves.append(possible_field)
                else:
                    break
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> bool:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        if not Chessboard.check_if_field_in_chessboard(dest_field):
            raise ValueError("destination field does not exist")
        if not dest_field.upper() in self.list_available_moves():
            return False
        else:
            return True


class King(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)

    def list_available_moves(self) -> list:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        available_moves = []
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
            possible_field = direction(self.current_field, distance_to_possible_field)
            if Chessboard.check_if_field_in_chessboard(possible_field):
                available_moves.append(possible_field)
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> bool:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        if not Chessboard.check_if_field_in_chessboard(dest_field):
            raise ValueError("destination field does not exist")
        if not dest_field.upper() in self.list_available_moves():
            return False
        else:
            return True


class Knight(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)

    def list_available_moves(self) -> list:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        available_moves = []
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
            if Chessboard.check_if_field_in_chessboard(possible_field):
                available_moves.append(possible_field)
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> bool:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        if not Chessboard.check_if_field_in_chessboard(dest_field):
            raise ValueError("destination field does not exist")
        if not dest_field.upper() in self.list_available_moves():
            return False
        else:
            return True


class Pawn(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)

    def list_available_moves(self) -> list:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        available_moves = [{"blacks": [], "whites": []}]
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
                if Chessboard.check_if_field_in_chessboard(possible_field_for_white):
                    available_moves[0]["whites"].append(possible_field_for_white)

            possible_field_for_black = direction_for_blacks(self.current_field, 1)
            if Chessboard.check_if_field_in_chessboard(possible_field_for_black):
                available_moves[0]["blacks"].append(possible_field_for_black)

        if current_row == 7:
            possible_field_for_white = direction_for_whites(self.current_field, 1)
            if Chessboard.check_if_field_in_chessboard(possible_field_for_white):
                available_moves[0]["whites"].append(possible_field_for_white)

            for distance_to_possible_field_for_blacks in [1, 2]:
                possible_field_for_black = direction_for_blacks(
                    self.current_field, distance_to_possible_field_for_blacks
                )
                if Chessboard.check_if_field_in_chessboard(possible_field_for_black):
                    available_moves[0]["blacks"].append(possible_field_for_black)

        if current_row in range(3, 7):
            possible_field_for_white = direction_for_whites(self.current_field, 1)
            if Chessboard.check_if_field_in_chessboard(possible_field_for_white):
                available_moves[0]["whites"].append(possible_field_for_white)

            possible_field_for_black = direction_for_blacks(self.current_field, 1)
            if Chessboard.check_if_field_in_chessboard(possible_field_for_black):
                available_moves[0]["blacks"].append(possible_field_for_black)

        if current_row == 1:
            return [{"whites": None, "blacks": []}]
        if current_row == 8:
            return [{"whites": [], "blacks": None}]
        return available_moves

    def validate_move(self, dest_field: str):
        dest_field = dest_field.upper()
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        if not Chessboard.check_if_field_in_chessboard(dest_field):
            raise ValueError("destination field does not exist")

        available_moves = self.list_available_moves()[0]
        whites_moves = available_moves["whites"]
        blacks_moves = available_moves["blacks"]

        is_move_valid_for_color = namedtuple("valid_move_for_color", ["white", "black"])

        if blacks_moves is None:
            return is_move_valid_for_color(False, None)

        elif whites_moves is None:
            return is_move_valid_for_color(None, False)

        elif dest_field not in whites_moves and dest_field in blacks_moves:
            return is_move_valid_for_color(False, True)

        elif dest_field in whites_moves and dest_field not in blacks_moves:
            return is_move_valid_for_color(True, False)

        else:
            return is_move_valid_for_color(False, False)


class Queen(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)

    def list_available_moves(self) -> list:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        available_moves = []
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
                if Chessboard.check_if_field_in_chessboard(possible_field):
                    available_moves.append(possible_field)
                else:
                    break
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> bool:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        if not Chessboard.check_if_field_in_chessboard(dest_field):
            raise ValueError("destination field does not exist")
        if not dest_field.upper() in self.list_available_moves():
            return False
        else:
            return True


class Rook(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)

    def list_available_moves(self) -> list:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        available_moves = []
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
                if Chessboard.check_if_field_in_chessboard(possible_field):
                    available_moves.append(possible_field)
                else:
                    break
        return sorted(available_moves)

    def validate_move(self, dest_field: str) -> bool:
        if not Chessboard.check_if_field_in_chessboard(self.current_field):
            raise ValueError("current field does not exist")
        if not Chessboard.check_if_field_in_chessboard(dest_field):
            raise ValueError("destination field does not exist")
        if not dest_field.upper() in self.list_available_moves():
            return False
        else:
            return True
