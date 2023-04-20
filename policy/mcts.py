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
        #探索済みノードをどう選択していくかUCT方策(ツリー方策)を用いて選択(or拡張)andロールアウトandバックアップ
        for _ in range(1000):
            selected_node = self.select()
            reward = selected_node.rollout()
            selected_node.backup(reward)
        best_child_node = self.best_child()
        return best_child_node.env.last_action

    def rollout(self):
        #シミュレーションフェーズで使用．とりあえずランダム方策(ロールアウト方策)を実装
        while not self.env.is_terminal() and not self.env.is_draw():
            actions = self.env.get_valid_actions()
            action = random.choice(actions)
            self.env.play(action)
        #終端状態時のプレイヤーが勝っていたら報酬1
        return 1 if self.env.is_winner(self.env.player) else 0

    def select(self):
        #根ノードから開始して，UCT方策(ツリー方策)を用いて葉ノードに向かって行動選択
        current_node = self
        while not current_node.env.is_terminal() and not current_node.env.is_draw():
            #子ノードの数よりも選択可能肢の方が多い場合は拡張
            #少ない場合は探索済みノードからUCT方策を用いて行動選択
            if len(current_node.children) < len(current_node.env.get_valid_actions()):
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node

    def expand(self):
        #選択された葉ノードから未探索の行動を取ることで子ノードを追加して，木を拡張する
        untried_actions = [a for a in self.env.get_valid_actions() if a not in [c.env.board for c in self.children]]
        action = random.choice(untried_actions)
        self.env.play(action)
        new_child = MonteCarloTreeSearch(self.env, parent=None)
        self.children.append(new_child)
        return new_child

    def backup(self, reward):
        #シミュレーションされて生成された収益を用いて，遷移軌跡の終端状態からバッグアップする
        self.visits += 1
        self.wins += reward
        if self.parent is not None:
            #親ノードがある場合は伝播させる
            self.parent.backup(reward)

    def best_child(self):
        #子ノードの中で一番良いノードを選択
        choices_weights = [(c.wins / c.visits) + np.sqrt((2 * np.log(self.visits) / c.visits)) for c in self.children]
        # return self.children[np.where(max(choices_weights) == choices_weights)[0]]
        return self.children[np.argmax(choices_weights)]