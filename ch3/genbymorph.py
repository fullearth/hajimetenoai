# -*- coding: utf-8 -*-

import random
import sys


FILENAME = "morph.txt"
MAXNO = 10000


# 形態素ファイルの読み込み
def readmorph():
    try:
        f = open(FILENAME, mode='r', encoding='cp932')
    except:
        print('error')
        sys.exit(1)
    db = []
    oldline = f.readline().rstrip()
    for i, line in enumerate(f):
        line = line.rstrip()
        db.append([oldline, line])
        oldline = line
        if i >= MAXNO:
            print("警告　形態素数を%d個に制限します" % MAXNO)
            break
    return db


# 開始文字列が何回含まれるか数える
def findch(startch, db):
    no = 0
    for morphs in db:
        if startch == morphs[0]:
            no += 1
    return no


def setrndstr(startch, db):
    return random.choice(db)[1]


def setnext(startch, db):
    lst = [morphset for morphset in db if morphset[0] == startch]
    return random.choice(lst)[1]


# 文の生成
def generates(startch, db):
    # 開始文字列を出力する
    print(startch, end="")
    while True:
        # 開始文字が何回含まれるか数える
        num = findch(startch, db)
        # その中からランダムに文字列を選ぶ
        if num != 0:
            startch = setnext(startch, db)
        else:
            startch = setrndstr(startch, db)
        # 文字を出力する
        print(startch, end="")
        if (startch == "．" or startch == "。"):
            break
    print("")


if __name__ == '__main__':
    db = readmorph()  # 2-gramファイルの読み込み
    workch = ""

    # 開始文字の決定
    print("開始文字列を入力してください")
    startch = input().rstrip()

    # 10回の分の生成
    for i in range(10):
        workch = startch
        generates(workch, db)
