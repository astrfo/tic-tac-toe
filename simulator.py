import numpy as np
from tictactoe import TicTacToe

class Simulator:
    def __init__(self):
        self.env = TicTacToe()

    def run(self):
        while not self.env.is_terminal() and not self.env.is_draw():
            action = np.random.randint(9)
            self.env.play(action)
            print(self.env.board)
