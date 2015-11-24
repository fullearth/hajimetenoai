# -*- coding: utf-8 -*-

"""
ランダムサーチプログラム rsearch.py
ランダムサーチによる解を探索します
todo: gene[POOLSIZE][RULESIZE][LOCUSSIZE]の単位の統一
      gene = gene  # 全体
      gene[i] = ?  # 遺伝子一つ
      gene[i][j] = ?  # ルール一つ
"""

from random import choice, random
import sys
from string import ascii_lowercase

POOLSIZE = 30
RULESIZE = 4
LOCUSSIZE = 4  # ひとつのルールが持つ遺伝子座の数

GMAX = 1000  # 打ち切り世代
MRATE = 0.1  # 突然変異率

LOWERLIMIT = 0  # 遺伝子を印字する最低適応度
MAXLINES = 64  # キーワードの組み合わせの最大数
LINESIZE = 64  # キーワードデータの行サイズ


# 遺伝子プールの初期化
def initgene():
    oneLocus = lambda: [choice(ascii_lowercase) for _ in range(LOCUSSIZE)]
    oneRule = lambda: [oneLocus() for _ in range(RULESIZE)]
    return [oneRule() for _ in range(POOLSIZE)]
    # gene = []
    # oneGene = lambda: [choice(ascii_lowercase) for _ in range(LOCUSSIZE)]
    # for i in range(POOLSIZE):
    #     gene.append([oneGene() for _ in range(RULESIZE)])
    # return gene


# ルールが何回データとマッチするかを計算
def score(singlerule, lines):
    score = 0
    for line in lines:
        localscore = len([s for s in singlerule if s in line])
        # print("localscore = %d" % localscore)
        if localscore >= LOCUSSIZE:  # 完全に一致
            score += 1
    return score


# i番目の染色体の適応度を計算
def fitness(sgene, lines):
    return sum([score(single, lines) for single in sgene])


# 遺伝子プールの出力
# todo: for3つ
def printgene(gene, lines):
    for i, singlegene in enumerate(gene):
        fvalue = fitness(singlegene, lines)
        if fvalue >= LOWERLIMIT:  # この条件を扁壺すると表示料を調整できます
            print("%3d : " % i, end="")
            for j, rule in enumerate(singlegene):
                for locus in rule:
                    print("%s " % locus, end="")
                if j < RULESIZE-1:
                    print(", ", end="")
            print("     %d" % fvalue)  # 適応度の出力


# 遺伝子プールの世代平均適応度の計算
def fave(gene, lines):
    return sum([fitness(one, lines) for one in gene]) / POOLSIZE


# キーワードデータの読み込み
# attention: python的には良くない名前
def readlines():
    lines = []
    for n, line in enumerate(sys.stdin):
        if n >= MAXLINES:
            print("警告　行数を%dに制限しました", n)
            break
        if len(line) <= 2:  # キーワードの記述されていない行の処理
            break
        lines.append(line.rstrip())
    return lines


# 突然変異
def mutation(gene):
    for single in gene:
        for rule in single:
            for i in range(LOCUSSIZE):
                if random() < MRATE:
                    rule[i] = choice(ascii_lowercase)


if __name__ == '__main__':
    lines = readlines()  # キーワードデータの読み込み
    gene = initgene()  # 遺伝子プールの初期化
    for generation in range(GMAX):
        print("第%d世代平均適応度 %f" % (generation, fave(gene, lines)))
        printgene(gene, lines)  # 遺伝子プールの出力
        mutation(gene)  # 突然変異
