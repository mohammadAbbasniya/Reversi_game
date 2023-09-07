from reversi_game import Player
from reversi_game import Reversi
import math


class AIPlayer(Player):

    def get_move(self, reversi: 'Reversi', possible_moves: 'list', pid: 'int'):
        self.pid = pid
        self.opid = reversi.opposite_pid(pid)
        move = self.minimax(reversi, 5, -math.inf, math.inf, True)[0]
        print(f'AI chose: {move[0]} {move[1]}')
        return move

    def fitness(self, reversi: 'Reversi'):
        # compute scores
        # +1    for each middle tail
        # +n/2  for each tail on board edges
        # +2n   for each tail on board corners

        n = reversi.n
        level = 0
        for i in range(n):
            for j in range(n):
                if reversi.board[i][j] != 0:
                    level += 1
        level_percent = level / n**2

        p1_score, p2_score = 0, 0
        for i in range(n):
            for j in range(n):
                score = 0
                if i == 0 or i == n-1:
                    if j == 0 or j == n-1:  # (i, j) is corner tail
                        score = n * (1 - level_percent)
                    else:  # (i, j) is edge tail
                        score = n/2 * (1 - level_percent)
                else:
                    if j == 0 or j == n-1:  # (i, j) is edge
                        score = n/2 * (1 - level_percent)
                    else:  # (i, j) is middle tail
                        score = 1

                # add score to player
                if reversi.board[i][j] == 1:
                    p1_score += score
                elif reversi.board[i][j] == 2:
                    p2_score += score

        if self.pid == 1:
            return p1_score - p2_score
        else:
            return p2_score - p1_score

    def minimax(self, reversi: 'Reversi', depth, alpha, beta, maximizing_player):
        is_terminal = reversi.is_completed()
        if depth == 0 or is_terminal:
            if is_terminal:
                p1_score, p2_score = reversi.p1_score, reversi.p2_score
                if p1_score > p2_score:
                    if self.pid == 1:
                        return None, 100000000000
                    else:
                        return None, -100000000000
                elif p1_score < p2_score:
                    if self.pid == 1:
                        return None, -100000000000
                    else:
                        return None, 100000000000
                else:
                    return None, 0

            else:  # Depth is zero
                return None, self.fitness(reversi)

        if maximizing_player:
            best_score = -math.inf
            best_move = None
            possible_moves = reversi.get_possible_moves(self.pid)
            for move in possible_moves:
                r_copy = reversi.copy()
                r_copy.apply_move(move, self.pid)
                new_score = self.minimax(r_copy, depth - 1, alpha, beta, False)[1]

                if new_score >= best_score:
                    best_score = new_score
                    best_move = move

                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break

            return best_move, best_score

        else:  # Minimizing player
            best_score = math.inf
            best_move = None
            possible_moves = reversi.get_possible_moves(self.opid)
            for move in possible_moves:
                r_copy = reversi.copy()
                r_copy.apply_move(move, self.opid)
                new_score = self.minimax(r_copy, depth - 1, alpha, beta, True)[1]

                if new_score <= best_score:
                    best_score = new_score
                    best_move = move

                beta = min(beta, best_score)
                if alpha >= beta:
                    break
            return best_move, best_score

