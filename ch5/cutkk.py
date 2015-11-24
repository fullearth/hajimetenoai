# -*- coding: utf-8 -*-


import re
import sys


# テキストを読み込む
def getsource():
    return sys.stdin.read()


# 全角文字のみ取り出す
def getwidechar(source):
    prog = re.compile('[^ぁ-んァ-ン一-龠ー。、，．]')
    return prog.sub('', source)


# 漢字かそれ以外かの判別
def iskanji(ch):
    prog = re.compile('[一-龠]')
    return bool(prog.search(ch))


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


# 語の切り出し
def outputmorph(target):
    last = typeset(target[0])
    for i, ch in enumerate(target):
        now = typeset(ch)
        if(now == 0 or now == 1):
            print(ch, end="")
        if(now != last and last != 2):
            print('')
        last = now


if __name__ == '__main__':
    # テキストを読み込む
    source = getsource()

    # 全角文字のみを取り出す
    target = getwidechar(source)

    # 語の切り出し
    outputmorph(target)
