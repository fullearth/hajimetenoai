# -*- coding: utf-8 -*-

"""
cutmorph.py
字種に基づく形態素の切り出し
テキストから全角データのみ抽出して形態素を切り出します
使い方
    cutnav (オプション)
    オプションの与え方
    nまたはなし     名詞の切り出し
    v               動詞の切り出し
    a               形容詞の切り出し
    d               形容動詞の切り出し
"""

import re
import sys


# テキストを読み込む
def getsource():
    return input()


# 全角文字のみ取り出す
def getwidechar(source):
    prog = re.compile('[^ぁ-んァ-ン一-龠。、，．]')
    return prog.sub('', source)


# 漢字かそれ以外かの判別
def iskanji(ch):
    prog = re.compile('[一-龠]')
    return bool(prog.search(ch))


# カタカナかそれ以外かの判別
def iskatakana(ch):
    prog = re.compile('[ァ-ン]')
    return bool(prog.search(ch))


# 字種の設定
def typeset(ch):
    if iskanji(ch):
        return 0  # 漢字は0
    elif iskatakana(ch):
        return 1  # カタカナは1
    else:
        return 2  # その他は2


# 名詞の切り出し
def outputnoun(target):
    last = typeset(target[0])
    for i, ch in enumerate(target):
        now = typeset(ch)
        if now != last and last == 0:
            print("")  # 区切りの改行を出力
            last = now
        if now == 0:
            print(ch, end="")
        last = now


# 動詞・形容詞・形容動詞・の切り出し
def outputp(target, string):
    last = typeset(target[0])
    k = ''
    for i, ch in enumerate(target):
        now = typeset(ch)
        if now == 0:
            k += ch  # 漢字を変数kに保存
        if now != last and last == 0:  # 漢字列の終わり
            if ch == string:
                k += ch
                print(k)  # 終端記号を出力
            k = ''  # 切り出し文字のリセット
        last = now


if __name__ == '__main__':
    # テキストを読み込む
    source = getsource()

    # 全角文字のみを取り出す
    target = getwidechar(source)

    # 名詞の切り出し
    if len(sys.argv) == 1:
        outputnoun(target)  # 名詞
    elif sys.argv[1] == 'n':
        outputnoun(target)  # 名詞
    elif sys.argv[1] == 'v':
        outputp(target, 'う')  # 動詞
    elif sys.argv[1] == 'a':
        outputp(target, 'い')  # 形容詞
    elif sys.argv[1] == 'd':
        outputp(target, 'だ')  # 形容動詞
