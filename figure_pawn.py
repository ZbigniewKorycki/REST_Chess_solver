from figure import Figure
from chessboard import Chessboard


class Pawn(Figure):
    def __init__(self, current_field: str):
        super().__init__(current_field)
        self.chessboard = Chessboard()

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass
