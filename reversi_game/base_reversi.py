class Reversi:
    directions = [(-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 0), (1, 1)]

    def __init__(self, n, board=None):
        self.n = n
        self.p1_score = 2
        self.p2_score = 2
        if board is not None:
            self.board = board
        else:
            self.board = [[0] * n for _ in range(n)]
            i, j = n // 2, n // 2 - 1
            self.board[i][i] = self.board[j][j] = 1  # 1 is data for player1
            self.board[i][j] = self.board[j][i] = 2  # 2 is data for player2

    def count_scores(self):
        self.p1_score, self.p2_score = 0, 0
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    self.p1_score += 1
                elif self.board[i][j] == 2:
                    self.p2_score += 1
        return self.p1_score, self.p2_score

    def is_valid(self, cell):
        return 0 <= cell[0] < self.n and 0 <= cell[1] < self.n

    def get_player_tiles(self, pid):
        tiles = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == pid:
                    tiles.append((i, j))
        return tiles

    def set_values(self, tails, value):
        for tail in tails:
            self.board[tail[0]][tail[1]] = value

    def opposite_pid(self, pid):
        if pid == 1:
            return 2
        elif pid == 2:
            return 1

    def is_completed(self):
        return self.p1_score == 0 or self.p2_score == 0 or \
               self.p1_score + self.p2_score >= self.n ** 2

    def apply_move(self, move, pid):
        (x, y) = move
        oppid = self.opposite_pid(pid)

        for d in Reversi.directions:
            next = (x + d[0], y + d[1])
            while self.is_valid(next) and self.board[next[0]][next[1]] == oppid:
                next = (next[0] + d[0], next[1] + d[1])

            if self.is_valid(next) and self.board[next[0]][next[1]] == pid:
                end = (next[0], next[1])
                next = (x, y)
                while next[0] != end[0] or next[1] != end[1]:
                    self.board[next[0]][next[1]] = pid
                    next = (next[0] + d[0], next[1] + d[1])

        self.count_scores()

    def get_possible_moves(self, pid):
        oppid = self.opposite_pid(pid)
        possible_moves = []
        for tile in self.get_player_tiles(pid):
            for d in Reversi.directions:
                next = (tile[0] + d[0], tile[1] + d[1])
                while self.is_valid(next) and self.board[next[0]][next[1]] == oppid:
                    next = (next[0] + d[0], next[1] + d[1])
                    if self.is_valid(next) and self.board[next[0]][next[1]] == 0:
                        possible_moves.append(next)

        return possible_moves

    def copy(self):
        new_board = [self.board[i].copy() for i in range(self.n)]
        return Reversi(n=self.n, board=new_board)
