# -*- coding: utf-8 -*-
import sys


# テキストを読み込む
lines = [line.rstrip() for line in sys.stdin]
# 整列
lines.sort()
# 出力
for line in lines:
    print(line)
