# -*- coding: utf-8 -*-

"""
gens1.py
書き換え規則による文の生成プログラムその１
書き換え規則Ａに従って文を生成します
書き換え規則　Ａ
    規則①      <文>→<名詞句><動詞句>
    規則②      <名詞句>→<形容詞句><名詞>は
    規則③      <名詞句>→<名詞>は
    規則④      <動詞句>→<動詞>
    規則⑤      <動詞句>→<形容詞>
    規則⑥      <動詞句>→<形容動詞>
    規則⑦      <形容詞句>→<形容詞><形容詞句>
    規則⑧      <形容詞句>→<形容詞>
"""

import random
import sys


NFILE = 'noun.txt'
VFILE = 'verb.txt'
AFILE = 'adj.txt'
DFILE = 'adjv.txt'


nlist = []
vlist = []
alist = []
dlist = []


# 規則4,5,6
def vp():
    lst = random.choice([vlist, alist, dlist])
    print(random.choice(lst), end='')


# 規則7,8
def ap():
    if random.randint(0, 1) > 0:
        ap()
        print(random.choice(alist), end='')
    else:
        print(random.choice(alist), end='')


# 規則2,3
def np():
    if random.randint(0, 1) > 0:
        ap()
        print(random.choice(nlist) + 'は', end='')
    else:
        print(random.choice(nlist) + 'は', end='')


# 規則1
def sentence():
    np()
    vp()


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
    alist = setlist(AFILE)
    dlist = setlist(DFILE)

    for i in range(50):
        sentence()
        print("。")
