# -*- coding: utf-8 -*-
import random
import sys


FILENAME = "2gram.txt"


# 返るのはリスト
def read2gram():
    with open(FILENAME) as f:
        db2gram = [line for line in f]
    return db2gram


# 開始文字が何回含まれるか数える
def findch(startch, db2gram):
    no = 0
    for ch in db2gram:
        if startch == ch[0]:
            no += 1
    return no


# startch = setrndstr
def setrndstr(startch, db2gram):
    point = random.randint(0, len(db2gram)-1)
    for i in range(len(db2gram)):
        if i == point:
            return db2gram[i][1]


# startch = setnext
def setnext(startch, db2gram, num):
    point = random.randint(0, num-1)
    no = 0
    # pointが0だった時にno == pointを補足できないバグを放置している
    for i in range(len(db2gram)):
        if startch == db2gram[i][0]:
            no += 1
        if no == point:
            return db2gram[i][1]


def generates(startch, db2gram):
    # 開始文字を出力する
    print(startch, end="")
    while True:
        # 開始文字が何回含まれるか数える
        num = findch(startch, db2gram)
        # その中からランダムに文字列を選ぶ
        if num != 0:
            startch = setnext(startch, db2gram, num)
        else:
            startch = setrndstr(startch, db2gram)
        # 文字を出力する
        print(startch, end="")
        if (startch == "．" or startch == "。"):
            break
    print("")


if __name__ == '__main__':
    db2gram = read2gram()  # 2-gramファイルの読み込み
    n = len(db2gram)
    workch = ""

    # オープニングメッセージ
    print("さくら：メッセージをどうぞ")
    while(True):
        try:
            line = input("あなた：")
        except EOFError:
            break
        print("\nさくら：", end="")
        startch = random.choice(line)
        generates(startch, db2gram)
    # エンディングメッセージ
    print("さくら：ばいば～い")
