# -*- coding: utf-8 -*-
import csv
from janome.tokenizer import Tokenizer

"""
与えられた文書からマルコフ連鎖のための辞書データを作成するためのプログラム
"""

t = Tokenizer()

# ファイルの読み込み
with open('./music_title_list_from_karatetsu.csv') as f:
    for token in t.tokenize(f.read()):
        print(token)
