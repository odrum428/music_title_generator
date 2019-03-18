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
with open('./music_title_list_from_karatetsu.csv', "r",  encoding="shift-jis") as f:
    # print(wakati(f.read()))
    # マルコフ連鎖用辞書作成
    markov = defaultdict(str)  # 辞書初期化
    w1, w2 = "", ""
    for word in wakati(f.read()): # それぞれの単語
        # print(word)
        # print('w1 && W2')
        if w1 and w2: # どちらも空じゃない
            if not (w1 == '\n'): #改行から続くのは次の曲タイトル
                if (w1, w2) not in markov:
                    # print(w1, w2)
                    markov[(w1, w2)] = []  # 登録して
                markov[(w1, w2)].append(word)  # 2単語の次の単語を追加する
        w1, w2 = w2, word

    #文章の自動生成
    count_n = 0  # いくつ曲のタイトルを生成させるか
    num_sentence = 10
    sentence = ""
    w1, w2 = random.choice(list(markov.keys()))
    while count_n < num_sentence:
        if (w1, w2) in markov: # そのキーの組み合わせがあったら
            tmp = random.choice(markov[(w1, w2)])
            # 2単語に続く候補の中からランダムに選択する
            # print(tmp)
            sentence += tmp
            if(tmp == '\n'):
                count_n += 1
            w1, w2 = w2, tmp
        else: # キーが存在しない場合
            w1, w2 = random.choice(list(markov.keys()))

    print(sentence)
