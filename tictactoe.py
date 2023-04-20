import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1
        self.last_action = None

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1
        self.last_action = None

    def play(self, action):
        row, col = action
        if self.board[row, col] == 0:
            self.board[row, col] = self.player
            self.player = 3 - self.player
            self.last_action = action
        else:
            raise ValueError(f"Cell ({row}, {col}) is already occupied.")

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

    def copy(self):
        new_env = TicTacToe()
        new_env.board = np.zeros((3, 3), dtype=int)
        new_env.player = self.player
        new_env.last_action = self.last_action
        return new_env

    def display(self):
        pass