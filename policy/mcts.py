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
            self.select()
            reward = self.rollout()
            self.backup(reward)
        # return self.best_child()の返り値でactionを返す？

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
        while not self.env.is_terminal() and not self.env.is_draw():
            #子ノードの数よりも選択可能肢の方が多い場合は拡張
            #少ない場合は探索済みノードからUCT方策を用いて行動選択
            if len(self.children) < len(self.env.get_valid_actions()):
                self.expand()
            else:
                self.best_child()

    def expand(self):
        #選択された葉ノードから未探索の行動を取ることで子ノードを追加して，木を拡張する
        pass

    def backup(self, reward):
        #シミュレーションされて生成された収益を用いて，遷移軌跡の終端状態からバッグアップする
        pass

    def best_child(self):
        pass