# -*- coding: utf-8 -*-
import sys


# 全角文字のみ取り出す
def getwidechar(source):
    return "".join([c for c in source if ord(c) > 255])


# 1-gramの出力
def outputtarget(target):
    for c in list(target):
        print(c)


if __name__ == '__main__':
    # テキストを読み込む
    # windowsコマンドプロンプトを想定。リダイレクトで標準入出力を繋ぐときはcp932のファイルにする。UTF-8だとsys.stdin.read()で死ぬ。
    source = sys.stdin.read()
    source = getwidechar(source)
    # 1-gramの出力
    outputtarget(source)
