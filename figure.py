from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, current_field: str):
        self.current_field = current_field.upper()

    @abstractmethod
    def list_available_moves(self):
        pass

    @abstractmethod
    def validate_move(self, dest_field: str) -> bool:
        pass





