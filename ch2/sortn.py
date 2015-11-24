# -*- coding: utf-8 -*-
import sys


lines = [line.rstrip() for line in sys.stdin]
lines.sort(key=lambda x: int(x.split()[0]), reverse=True)
for line in lines:
    print(line)
