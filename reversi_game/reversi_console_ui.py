from reversi_game import Player
from reversi_game import Reversi


class ReversiConsoleUI:
    def __init__(self, n: int, player1: Player, player2: Player):
        self.reversi = Reversi(n)
        self.player1 = player1
        self.player2 = player2

    def get_flag(self, d):
        if d == 1:  # player 1
            return self.player1.flag
        elif d == 2:  # player 2
            return self.player2.flag
        elif d == 3:  # hint
            return '.'
        else:
            return ' '

    def display_board(self):
        n = self.reversi.n
        print('\n\n', end='   ')
        for i in range(n):
            print(f'  {i :2d}', end='')
        print('\n    ┌' + '───┬' * (n - 1) + '───┐')
        for i in range(n):
            print(f' {i :2d} │', end='')
            for j in range(n):
                print(f' {self.get_flag(self.reversi.board[i][j])} │', end='')
            print()
            if i < n - 1:
                print('    │' + '───┼' * (n - 1) + '───┤')
        print('    └' + '───┴' * (n - 1) + '───┘')
        print('    ┌──────────────────┬──────────────────┐')
        print(f'    │ Player1 ({self.get_flag(1)}): {self.reversi.p1_score:3d} │ Player2 ({self.get_flag(2)}): {self.reversi.p2_score:3d} │')
        print('    └──────────────────┴──────────────────┘')

    def run(self):
        while not self.reversi.is_completed():
            p1_possible_moves = self.reversi.get_possible_moves(1)
            if len(p1_possible_moves) > 0:
                self.reversi.set_values(p1_possible_moves, 3)  # set hints
                self.display_board()
                self.reversi.set_values(p1_possible_moves, 0)  # remove hints
                print(f'[ Player1 ({self.get_flag(1)}) Turn: ]')
                move = self.player1.get_move(self.reversi, p1_possible_moves, 1)
                self.reversi.apply_move(move, 1)

            p2_possible_moves = self.reversi.get_possible_moves(2)
            if len(p2_possible_moves) > 0:
                self.reversi.set_values(p2_possible_moves, 3)  # set hints
                self.display_board()
                self.reversi.set_values(p2_possible_moves, 0)  # remove hints
                print(f'[ Player2 ({self.get_flag(2)}) Turn: ]')
                move = self.player2.get_move(self.reversi, p2_possible_moves, 2)
                self.reversi.apply_move(move, 2)

            if len(p1_possible_moves) == len(p2_possible_moves) == 0:
                # break if both players have no choice
                break

        # display final results after terminating game
        self.display_board()
        if self.reversi.p1_score > self.reversi.p2_score:
            print(f'    [ Player1 ({self.get_flag(1)}) Won ! ]')
        elif self.reversi.p1_score < self.reversi.p2_score:
            print(f'    [ Player2 ({self.get_flag(2)}) Won ! ]')
        else:
            print('    [ Draw ! ]')

