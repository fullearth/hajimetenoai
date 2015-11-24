# -*- coding: utf-8 -*-

"""
wavファイル生成プログラム
python標準のwaveを使用
16bit 8KHz mono
"""

import wave
import sys
import array


# テキストファイルの読み込み
def readdata():
    return [int(line) for line in sys.stdin]


def makeheader(f):
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(8000)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python makewav.py out')
        sys.exit(1)
    # tryとかやらないで雑にopen
    f = wave.open(sys.argv[1], mode="wb")

    # 数値(テキスト)の読み込み
    # writeframes用にbytes-like objectなオブジェクトに変換
    sounddata = array.array('h', readdata())

    # ヘッダ情報の出力
    makeheader(f)
    # 出力
    f.writeframes(sounddata)
    f.close()
