# -*- coding: utf-8 -*-

"""
ai3.py
形態素の連鎖により文を作成する人工無能プログラムです
形態素の連鎖が格納されたファイルmorph.txtを用います
"""

import random
import sys
import re


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


# 開始文字列の決定
def setstartch(line):
    # 漢字以外の読み飛ばし
    match = re.search('[一-龠]+', line)
    if match is None:
        return '人工知能'
    else:
        # 漢字の抽出
        return match.group(0)


if __name__ == '__main__':
    db = readmorph()  # 形態素ファイルの読み込み

    # オープニングメッセージ
    print("さくら：メッセージをどうぞ")
    while(True):
        try:
            line = input("あなた：")
        except EOFError:
            break
        print("\nさくら：", end="")
        startch = setstartch(line)
        generates(startch, db)
    # エンディングメッセージ
    print("さくら：ばいば～い")
