# -*- coding: utf-8 -*-
import csv
from janome.tokenizer import Tokenizer

"""
与えられた文書からマルコフ連鎖のための辞書データを作成するためのプログラム
"""

t = Tokenizer()

# Janomeを使用してテキストデータを単語に分割する
def wakati(text):
    text = text.replace('\n', '')  # 改行を削除
    text = text.replace('\u3000', '')  # 全角の空白を削除
    t = Tokenizer()
    result = t.tokenize(text, wakati=True)
    return result

# ファイルの読み込み
with open('./music_title_list_from_karatetsu.csv') as f:
    print(wakati(f.read()))

