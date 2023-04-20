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
            if self.env.player == 1:
                action = self.get_human_input()
            else:
                action = self.policy.uct_search()
            self.env.play(action)
            print(self.env.board)
            print('=========================')

        if self.env.is_winner(player=1):
            print(f'Player wins!!')
        elif self.env.is_winner(player=2):
            print(f'AI wins!!')
        else:
            print('Draw!!')

    def get_human_input(self):
        while True:
            row, col = map(int, input('Enter row and column: ').split())
            if (row, col) in self.env.get_valid_actions():
                return (row, col)
            else:
                print(f'Cell ({row}, {col}) is not a valid action. Please try again.')