# -*- coding: utf-8 -*-
import sys


# オープニングメッセージ
print('さくら：メッセージをどうぞ\n', end="")
print('あなた：')
# 会話しましょう
# windowsコマンドプロンプトでのEOF入力はCTRL+Z
for line in sys.stdin:
    print('さくら：ふ～ん、それで？\n', end="")
    print('あなた：', end="")

# エンディングメッセージ
print('さくら：ばいば～い\n')
