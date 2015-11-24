# -*- coding: utf-8 -*-

"""
cutmorph.py
字種に基づく形態素の切り出し
テキストから全角データのみ抽出して形態素を切り出します
"""

import re


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


# 句読点の検出
def ispunct(ch):
    if ch in ['．', '。', '，', '、']:
        return True  # 句読点ならTrue
    else:
        return False


# 形態素の切り出し
def outputmorph(target):
    last = typeset(target[0])
    for i, ch in enumerate(target):
        if not ispunct(ch):
            now = typeset(ch)
            if now != last:
                print("")  # 区切りの改行を出力
                last = now
            print(ch, end="")
        else:
            print("")  # 区切りの改行を出力
            last = typeset(target[min(i+1, len(target)-1)])

if __name__ == '__main__':
    # テキストを読み込む
    source = getsource()

    # 全角文字のみを取り出す
    target = getwidechar(source)

    # 形態素の切り出し
    outputmorph(target)
