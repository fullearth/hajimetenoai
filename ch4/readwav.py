# -*- coding: utf-8 -*-

"""
wavファイルはSoftalkで生成したものを使用
16bit 8KHz モノラル
1サンプリング当たり2byte
"""

import sys
from struct import unpack


# dataチャンクまで読み飛ばす
def skipheader(f):
    ch1 = ch2 = ch3 = ch4 = ''
    while True:
        if(ch4 == bytes(b'a') and ch3 == bytes(b't') and
           ch2 == bytes(b'a') and ch1 == bytes(b'd')):
            break
        ch1 = ch2
        ch2 = ch3
        ch3 = ch4
        ch4 = f.read(1)
        if ch4 == bytes(b''):
            break
    f.read(4)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('arguments error')
        exit(1)
    try:
        f = open(sys.argv[1], mode=('rb'))
    except Exception as e:
        print(e)
        exit(1)
    skipheader(f)
    for ch in iter(lambda: f.read(2), bytes(b'')):
        print(unpack('<h', ch)[0])
