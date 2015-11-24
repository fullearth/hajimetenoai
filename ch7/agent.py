# -*- coding: utf-8 -*-
"""
強化学習によるじゃんけんエージェントプログラム(環境付き) agent.py
正しく動いているか検証してない
"""

from random import randint

GU = 0
CYOKI = 1
PA = 2
INITVAL = 10
FILENAME = "int.txt"
HANDSFILENAME = "hands.txt"


# 学習
def learning(reward, last_my, last_opp, q, fp):
    for i in range(3):
        if i == last_my:
            alpha = 1
        else:
            alpha = -1
        # 報酬に基づいてqを更新
        if q[last_opp][i] + alpha * reward > 0:
            q[last_opp][i] += alpha * reward
        # ファイルへの内部状態の書き出し
        for q_ in q:
            for status in q_:
                fp.write("%d " % status)
        fp.write("\n")


# ルーレットを回して手を選ぶ
def roulette(pq):
    step = randint(0, sum(pq)-1)
    acc = 0
    point = 0
    while acc <= step:
        acc += pq[point]
        point += 1
    return point - 1


# 行動選択
def selectaction(opphand, q):
    return roulette(q[opphand])


# 報酬の設定
def setreward(opphand, last_my):
    rtable = [[0, -1, 1], [1,  0, -1], [-1, 1, 0]]
    return rtable[opphand][last_my]


if __name__ == '__main__':
    q = [[INITVAL for _ in range(3)] for _ in range(3)]
    # withもtryも使わない
    fp = open(FILENAME, mode='w', encoding='cp932')
    handsfp = open(HANDSFILENAME, mode='r', encoding='cp932')
    last_my = last_opp = GU  # 最初はグー
    # じゃんけんの繰り返し
    for line in handsfp:
        opphand = int(line.rstrip())
        reward = setreward(opphand, last_my)
        if reward != 0:
            # 報酬に基づく学習
            learning(reward, last_my, last_opp, q, fp)
        print("%d %d " % (opphand, reward), end="")  # 前回の結果の出力
        # 次の行動を決定する
        last_my = selectaction(opphand, q)
        print("%d" % last_my)
        last_opp = opphand  # 前回の手を覚えておく
