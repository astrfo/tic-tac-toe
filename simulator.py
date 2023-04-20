import numpy as np
from tictactoe import TicTacToe
from policy.mcts import MonteCarloTreeSearch

class Simulator:
    def __init__(self):
        self.env = TicTacToe()
        self.policy = MonteCarloTreeSearch(self.env)

    def run(self):
        while not self.env.is_terminal() and not self.env.is_draw():
            action = self.policy.uct_search()
            self.env.play(action)
            print(self.env.board)
