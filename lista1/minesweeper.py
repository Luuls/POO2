from typing import Callable
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
        self.__game_over_method = game_over_method

    def action(self):
        self.__game_over_method()


class BlankCell:
    def __init__(self, reveal_space_method: Callable, n_bombs_around: int):
        self.__n_bombs_around = n_bombs_around
        self.__reveal_space_method = reveal_space_method

    def get_n_bombs_around(self) -> int:
        return self.__n_bombs_around

    def action(self) -> None:
        self.__reveal_space_method()

class Map:
    def __init__(self, size: int):
        self.__size = size

        self.__cells: list[list[Cell]]
        self.generate_map()
        
    def get_size(self):
        return self.__size

    def reveal_space_from_blank_cell(self, cell_position: tuple[int, int]):
        ...

    def print(self):
        ...

    def generate_map(self):
        # passa Game.game_over para uma célula se ela for uma bomba
        # passa self.reveal_space_from_blank_cell se ela for uma célula comum
        ...

class Game:
    def __init__(self):
        self.__is_running = False
        self.__map = Map(20)
        self.__player_bet: tuple[int, int]

        self.__states = {
            'menu': self.menu,
            'in_game': self.in_game,
            'game_over': self.game_over
        }

        self.__state = self.__states['menu']

    def handle_player_bet(self):
        ...

    def run(self) -> None:
        ...

    def menu(self) -> None:
        ...

    def in_game(self) -> None:
        ...

    def game_over(self) -> None:
        ...

    def change_state(self, new_state: str) -> None:
        ...
