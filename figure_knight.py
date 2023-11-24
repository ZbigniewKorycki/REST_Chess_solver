from figure import Figure


class Knight(Figure):

    def __init__(self, current_field: str):
        super().__init__(current_field)

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass