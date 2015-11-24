# -*- coding: utf-8 -*-
import sys
import collections


# 読み込み
lines = [line.rstrip() for line in sys.stdin]
# 重複数え上げ
counted_d = collections.Counter(lines)

for k, v in counted_d.items():
    print("%d\t%s" % (v, k))
