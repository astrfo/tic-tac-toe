import random
import numpy as np

class MonteCarloTreeSearch:
    def __init__(self, env, parent=None):
        self.env = env
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def uct_search(self):
        for _ in range(1000):
            selected_node = self.select()
            reward = selected_node.rollout()
            selected_node.backup(reward)
        best_child_node = self.best_child()
        return best_child_node.env.last_action

    def rollout(self):
        copy_env = self.env.copy()
        while not copy_env.is_terminal():
            actions = copy_env.get_valid_actions()
            action = random.choice(actions)
            copy_env.play(action)
        return 1 if copy_env.is_winner(copy_env.player) else 0

    def select(self):
        current_node = self
        while not current_node.env.is_terminal():
            if len(current_node.children) < len(current_node.env.get_valid_actions()):
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node

    def expand(self):
        untried_actions = [a for a in self.env.get_valid_actions() if a not in [c.env.last_action for c in self.children]]
        action = random.choice(untried_actions)
        child_env = self.env.copy()
        child_env.play(action)
        new_child = MonteCarloTreeSearch(child_env, parent=self)
        self.children.append(new_child)
        return new_child

    def backup(self, reward):
        self.visits += 1
        self.wins += reward
        if self.parent is not None:
            self.parent.backup(reward)

    def best_child(self):
        choices_weights = [(c.wins / c.visits) + np.sqrt((2 * np.log(self.visits) / c.visits)) for c in self.children]
        return self.children[np.argmax(choices_weights)]