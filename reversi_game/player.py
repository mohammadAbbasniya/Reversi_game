from abc import ABC, abstractmethod
from reversi_game import Reversi


class Player(ABC):
    def __init__(self, flag):
        self.flag = flag

    @abstractmethod
    def get_move(self, reversi: 'Reversi', possible_moves: 'list', pid: 'int'):
        pass
