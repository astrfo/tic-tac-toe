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
                action = self.get_human_input()
            else:
                #AI側が入力
                action = self.policy.uct_search()
            self.env.play(action)

        if self.env.is_draw():
            print('Draw!!')
        else:
            print(f'Player {3 - self.env.player} wins!!')

    def get_human_input(self):
        while True:
            row, col = map(int, input('Enter row and column: ').split())
            if (row, col) in self.env.get_valid_actions():
                return (row, col)
            else:
                print(f'Cell ({row}, {col}) is not a valid action. Please try again.')