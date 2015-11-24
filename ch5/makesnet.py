# -*- coding: utf-8 -*-


import sys


# テキストを読み込む
def getsource():
    f = open('kk.txt', mode='r', encoding='cp932')
    lst = [line.rstrip() for line in f]
    f.close()
    # 読み込み処理
    # 余った分は切り捨て
    # リストを2つずつのタプルのリストに分割するイディオム的なもの
    # list(zip(*[iter([1,2,3,4,5,6,7,8,9])]*2)) -> [(1,2), (3,4), (5,6), (7,8)]
    # todo: MAXLINEの処理
    return [list(zipped) for zipped in zip(*[iter(lst)]*2)]


# 意味ネットワークの探索
# 対応する語が見つかったらそのインデックス、見つからなかったらfalseが返る
def searchword(semnet, line, flag):
    for i, s in enumerate(semnet):
        if s[0] == line and not flag[i]:
            flag[i] = True
            return i
    return False


# 連想の処理
def searchsnet(semnet, line):
    # フラグの初期化
    flag = [False] * len(semnet)
    pos = searchword(semnet, line, flag)
    while pos:
        print("%sは%s、" % (line, semnet[pos][1]))
        line = semnet[pos][1]
        pos = searchword(semnet, line, flag)
    print("%sは・・・わからない！" % line)


if __name__ == '__main__':
    semnet = getsource()
    print("%d個の意味ネットワークを読み込みました" % len(semnet))

    # 意味ネットワークを検索する
    print("連想を開始する単語を入力してください。")
    # 連想しましょう
    for line in sys.stdin:
        searchsnet(semnet, line.rstrip())
        print("連想を開始する単語を入力してください。")
    print('処理を終わります。')
