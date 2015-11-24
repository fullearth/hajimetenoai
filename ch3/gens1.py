# -*- coding: utf-8 -*-

"""
gens1.py
書き換え規則による文の生成プログラムその１
書き換え規則Ａに従って文を生成します
書き換え規則　Ａ
    規則①      <文>→<名詞句><動詞句>
    規則②      <名詞句>→<名詞>は
    規則③      <動詞句>→<動詞>
"""

import random
import sys


NFILE = 'noun.txt'
VFILE = 'verb.txt'


# 規則③      <動詞句>→<動詞>
def vp(vlist):
    print(random.choice(vlist), end='')


# 規則②      <名詞句>→<名詞>は
def np(nlist):
    print(random.choice(nlist) + 'は', end='')


# 規則①      <文>→<名詞句><動詞句>
def sentence(nlist, vlist):
    np(nlist)
    vp(vlist)


# 名詞リスト・動詞リストの読み込み
def setlist(filename):
    try:
        f = open(filename, mode='r', encoding='utf-8')
        l = [line.rstrip() for line in f]
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        f.close()
    return l


if __name__ == '__main__':
    nlist = setlist(NFILE)
    vlist = setlist(VFILE)

    for i in range(50):
        sentence(nlist, vlist)
        print("。")
