import random
import numpy as np

class MonteCarloTreeSearch:
    def __init__(self, env):
        self.env = env

    def uct_search(self):
        #探索済みノードをどう選択していくかUCT方策(ツリー方策)を用いて選択or拡張
        pass

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
        pass

    def expand(self):
        #選択された葉ノードから未探索の行動を取ることで子ノードを追加して，木を拡張する
        pass

    def backup(self):
        #シミュレーションされて生成された収益を用いて，遷移軌跡の終端状態からバッグアップする
        pass