import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1

    def play(self, action):
        row = action // 3
        col = action % 3
        if self.board[row, col] == 0:
            self.board[row, col] = self.player
            self.player = 3 - self.player

    def get_valid_actions(self):
        return list(zip(*np.where(self.board == 0)))

    def is_terminal(self):
        return self.is_winner(1) or self.is_winner(2) or self.is_draw()

    def is_winner(self, player):
        for i in range(3):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

    def is_draw(self):
        return not np.any(self.board == 0)

    def display(self):
        pass