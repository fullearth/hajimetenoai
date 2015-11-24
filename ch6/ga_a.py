# -*- coding: utf-8 -*-

"""
遺伝的アルゴリズムによる探索プログラム ga_a.py
一様交叉、突然変異、選択を行います
todo: gene[POOLSIZE][RULESIZE][LOCUSSIZE]の単位の統一
      gene = gene  # 全体
      gene[i] = singlegene  # 遺伝子一つ
      gene[i][j] = ?  # ルール一つ
      gene[i][j][k] = locus  # 遺伝子座一つ
"""

from random import choice, random, randint
import sys
from string import ascii_uppercase

POOLSIZE = 30
RULESIZE = 4
LOCUSSIZE = 4  # ひとつのルールが持つ遺伝子座の数

GMAX = 300  # 打ち切り世代
MRATE = 0.01  # 突然変異率

LOWERLIMIT = 0  # 遺伝子を印字する最低適応度
MAXLINES = 64  # キーワードの組み合わせの最大数
LINESIZE = 64  # キーワードデータの行サイズ


# 遺伝子プールの初期化
def initgene():
    oneLocus = lambda: [choice(ascii_uppercase) for _ in range(LOCUSSIZE)]
    oneRule = lambda: [oneLocus() for _ in range(RULESIZE)]
    return [oneRule() for _ in range(POOLSIZE)]
    # gene = []
    # oneGene = lambda: [choice(ascii_uppercase) for _ in range(LOCUSSIZE)]
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
def mutation(midgene):
    for single in midgene:
        for rule in single:
            for i in range(LOCUSSIZE):
                if random() < MRATE:
                    rule[i] = choice(ascii_uppercase)


# ルーレットを回してひとつ遺伝子を選ぶ
def roulette(fvalue, sumf, point):
    acc = 0
    step = randint(0, sumf)
    # ポインタのインクリメント
    incpoint = lambda x: 0 if x + 1 >= POOLSIZE*2 else x + 1
    while acc < step:
        point = incpoint(point)
        acc += fvalue[point]
    fvalue[point] = 0  # 2度選ばれないようにする
    return point


# 選択
def selection(midgene, lines):
    # setfvalue
    fvalue = [fitness(single, lines) + 1 for single in midgene]
    sumf = sum(fvalue)  # 適応度の合計値を計算
    gene = []
    point = 0  # ???
    for _ in range(POOLSIZE):
        midpoint = roulette(fvalue, sumf, point)
        gene.append(midgene[midpoint])
    return gene


# ポインタのインクリメント(groulette用)
# def gincpoint(point):
#     point += 1
#     if point >= POOLSIZE:
#         point = 0
#     return point


# ルーレットを回してひとつ遺伝子を選ぶ(交叉用)
def groulette(fvalue, sumf, point):
    acc = 0
    step = randint(0, sumf)
    # ポインタのインクリメント(groulette用)
    gincpoint = lambda x: 0 if x + 1 >= POOLSIZE else x + 1
    while acc < step:
        point = gincpoint(point)
        acc += fvalue[point]
    return point


# 一様交叉
# 遺伝子2個から新しい遺伝子が2個タプルで返る
# zipしてごにょごにょしたわりにはわかりにくくなった
# todo: もっとかっこよく
# singlecrossover([list("abcd"), list("efgh")], [list("ijkl"), list("mnop")])
"""
    遺伝子座4、ルールの数2の遺伝子をp1, p2とすると
    p1 = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]
    p2 = [['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
    rulepair = zip(p1, p2)  # 各ルールのペア
    -> [(['a', 'b', 'c', 'd'], ['i', 'j', 'k', 'l']),
        (['e', 'f', 'g', 'h'], ['m', 'n', 'o', 'p'])
       ]
    locuspairs = [zip(a, b) for a, b in rulepair]  # それぞれの遺伝子座の可能性
    -> [
         [('a', 'i'), ('b', 'j'), ('c', 'k'), ('d', 'l')],
         [('e', 'm'), ('f', 'n'), ('g', 'o'), ('h', 'p')]
       ]
"""


def singlecrossover(p1, p2):
    rulepair = zip(p1, p2)
    locuspairs = [zip(a, b) for a, b in rulepair]
    midgene1 = []
    midgene2 = []
    for pairs in locuspairs:
        midrule1 = []
        midrule2 = []
        for a, b in pairs:
            if choice([True, False]):
                midrule1.append(a)
                midrule2.append(b)
            else:
                midrule1.append(b)
                midrule2.append(a)
        midgene1.append(midrule1)
        midgene2.append(midrule2)
    return (midgene1, midgene2)


# 交叉
def crossover(gene, lines):
    gfvalue = [fitness(singlegene, lines) + 1 for singlegene in gene]
    gsumf = sum(gfvalue)  # 適応度の合計値を計算
    point1 = 0
    point2 = 0
    midgene = []
    for i in range(POOLSIZE):
        point1 = groulette(gfvalue, gsumf, point2)
        point2 = groulette(gfvalue, gsumf, point1)
        a, b = singlecrossover(gene[point1],
                               gene[point2])
        midgene.append(a)
        midgene.append(b)
    return midgene


if __name__ == '__main__':
    lines = readlines()  # キーワードデータの読み込み
    gene = initgene()  # 遺伝子プールの初期化
    for generation in range(GMAX):
        print("第%d世代平均適応度 %f" % (generation, fave(gene, lines)))
        printgene(gene, lines)  # 遺伝子プールの出力
        midgene = crossover(gene, lines)
        mutation(midgene)  # 突然変異
        # print("mid")
        # printgene(midgene, lines)
        # print("----")
        gene = selection(midgene, lines)
    print("第%d世代平均適応度 %f" % (GMAX, fave(gene, lines)))
    printgene(gene, lines)  # 遺伝子プールの出力
