# -*- coding: utf-8 -*-
import csv
from janome.tokenizer import Tokenizer
import random
from collections import defaultdict # キーが存在しなくても辞書データを更新できる

"""
与えられた文書からマルコフ連鎖のための辞書データを作成するためのプログラム
"""

t = Tokenizer()
text = ""

# Janomeを使用してテキストデータを単語に分割する
def wakati(text):
    text = text.replace('\u3000', '')  # 全角の空白を削除
    t = Tokenizer()
    result = t.tokenize(text, wakati=True)
    return result

# ファイルの読み込み
with open('./music_title_list_from_karatetsu.csv') as f:
    print(wakati(f.read()))

