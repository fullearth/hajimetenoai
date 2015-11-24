# -*- coding: utf-8 -*-

"""
ai6.py
学習による語彙を増やす人工無能プログラム
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
    # ai3.pyからの変更点
    # todo: withかfinally
    f.close()
    # 変更点終わり
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


# 漢字かそれ以外かの判別
def iskanji(ch):
    prog = re.compile('[一-龠]')
    return bool(prog.search(ch))


# 開始文字列の決定
def setstartch(line):
    # 漢字以外の読み飛ばし
    match = re.search('[一-龠]+', line)
    if match is None:
        return '人工知能'
    else:
        # 漢字の抽出
        return match.group(0)


# 以下、ai3.pyからの変更点
# 以下はcutm_p.pyからの関数追加
# カタカナかそれ以外かの判別
def iskatakana(ch):
    prog = re.compile('[ァ-ンー]')
    return bool(prog.search(ch))


# 字種の設定
def typeset(ch):
    if iskanji(ch):
        return 0  # 漢字は0
    elif iskatakana(ch):
        return 1  # カタカナは1
    else:
        return 2  # その他は2


# 句読点の検出
def ispunct(ch):
    if ch in ['．', '。', '，', '、']:
        return True  # 句読点ならTrue
    else:
        return False


# 全角文字のみ取り出す
def getwidechar(source):
    prog = re.compile('[^ぁ-んァ-ン一-龠ー。、，．]')
    return prog.sub('', source)
# ここまではcutm_p.pyの関数の追加


# 形態素の切り出し
# この関数はcutm_p.pyの同名の関数を改造したものです
# 句読点無しの文章を入力してはならない。これはai6.cの仕様である。
def outputmorph(target, f):
    last = typeset(target[0])
    for i, ch in enumerate(target):
        if not ispunct(ch):
            now = typeset(ch)
            if now != last:  # 字種が変わっている
                f.write("\n")  # 区切りの改行を出力
                last = now
            f.write(ch)
        else:
            f.write("\n")  # 区切りの改行を出力
            f.write(ch + "\n")
            last = typeset(target[min(i+1, len(target)-1)])


# 利用者の入力から形態素ファイルを更新する
def addmorph(line):
    with open(FILENAME, mode='a', encoding='cp932') as f:
        target = getwidechar(line)
        outputmorph(target, f)
# 以上でai3.pyプログラムからの変更点終わり


if __name__ == '__main__':
    # オープニングメッセージ
    print("さくら：メッセージをどうぞ")
    while(True):
        try:
            line = input("あなた：")
        except EOFError:
            break
        # ai3.pyからの変更点
        addmorph(line)
        # 形態素ファイルの読み込み
        db = readmorph()
        # 変更点終わり
        print("\nさくら：", end="")
        startch = setstartch(line)
        generates(startch, db)
    # エンディングメッセージ
    print("さくら：ばいば～い")
