# -*- coding: utf-8 -*-

"""
しゃべる人工無能プログラム
このプログラムは音声で返答する人工無能です
ただし、返答の内容は固定です
pyaudioが必要
pip install pyaudio
"""

import pyaudio
import wave
import random


# 人工無能の返答作成(ランダム)
def reply():
    CHUNK = 1024
    # 返答リスト
    replyList = [{'text': 'ふ～ん、それで？', 'file': 'fuun.wav'},
                 {'text': 'そうなの？', 'file': 'sounano.wav'},
                 {'text': 'そうかもしれないわね・・・', 'file': 'soukamo.wav'}]
    now = random.choice(replyList)
    print('さくら：' + now['text'])
    # ここから音声
    wf = wave.open(now['file'], 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    # play stream
    data = wf.readframes(CHUNK)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    # stop stream
    stream.stop_stream()
    stream.close()
    # close pyaudio
    p.terminate()
    wf.close()


if __name__ == '__main__':
    # オープニングメッセージ
    print('さくら：メッセージをどうぞ')
    while True:
        try:
            s = input('あなた：')
        except EOFError:
            break
        reply()
    # エンディングメッセージ
    print('さくら：ばいば～い')
