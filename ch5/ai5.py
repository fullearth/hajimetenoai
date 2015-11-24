# -*- coding: utf-8 -*-

"""
ai5.py
プロダクションルールを用いた人工無能
プロダクションルールを記述したファイルrule.txtが必要です
"""

import re
import random


FILENAME = 'rule.txt'


# プロダクションルールを格納するクラス
class prule:
    def __init__(self, r1, r2, r3, r4, action):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        self.action = action
        if len(self.r1) >= 1 and self.r1 != '-':
            if self.r2 == '-':
                self.r2 = self.r1
            if self.r3 == '-':
                self.r3 = self.r2
            if self.r4 == '-':
                self.r4 = self.r3


# 入力にマッチするルールを探す
def rulematch(rule, line):
    if(re.search(rule.r1, line) and
       re.search(rule.r2, line) and
       re.search(rule.r3, line) and
       re.search(rule.r4, line)):
        return True  # 合致した
    else:
        return False  # 合致しない


# 応答文の生成
def answer(rule, line):
    # マッチするルールだけ取り出す
    matchedRules = [r for r in rule if rulematch(r, line)]
    if len(matchedRules) == 0:
        print('どうぞ続けてください')
    else:
        print(random.choice(matchedRules).action)


# テキストを読み込む
# 処理の一部はpruleの__init__にまかせる
def readrule():
    with open(FILENAME, mode='r', encoding='cp932') as f:
        return [prule(*line.split()) for line in f]


if __name__ == '__main__':
    rule = readrule()
    # オープニングメッセージ
    print('さくら：さて、どうしました？')
    while True:
        try:
            line = input('あなた：')
        except EOFError:
            break
        print('さくら：', end='')
        answer(rule, line)  # プロダクションルールによる応答文生成
    # エンディングメッセージ
    print('さくら：それではお話を終わりましょう')
