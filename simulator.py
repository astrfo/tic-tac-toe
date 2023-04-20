import numpy as np
from tictactoe import TicTacToe
from policy.mcts import MonteCarloTreeSearch

class Simulator:
    def __init__(self):
        self.env = TicTacToe()
        self.policy = MonteCarloTreeSearch(self.env)

    def run(self):
        self.env.reset()
        while not self.env.is_terminal():
            print(self.env.board)
            if self.env.player == 1:
                #人間側が入力
                pass
            else:
                #AI側が入力
                action = self.policy.uct_search()
            self.env.play(action)