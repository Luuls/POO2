from abc import ABC, abstractmethod
class Cell(ABC):
    def __init__(self, char_to_show: str):
        self.__char = char_to_show
        self.__visible = False

    def get_char(self) -> str:
        return self.__char

    def is_visible(self):
        return self.__visible

    @abstractmethod
    def action(self):
        ...


class BombCell(Cell):
    def __init__(self, game_over_method: Callable, char_to_show: str = '@'):
        Cell.__init__(self, char_to_show)
        self.__game_over_method

    def action(self):
        self.__game_over_method()


class BlankCell:
    def __init__(self, n_bombs_around): int:
        self.__n_bombs_around = n_bombs_around

    def get_n_bombs_around(self) -> int:
        return self.__n_bombs_around

    def action(self) -> None:
        ...


class Map:
    def __init__(self, size: int):
        self.__size = size
