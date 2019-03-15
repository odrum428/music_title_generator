# 曲のタイトルデータを取得して、ファイルに落としてくれるプログラム

import requests
import csv
import re
from bs4 import BeautifulSoup

URL = 'https://www.karatetsu.com/animegame/pickup/ranking.php'

response = requests.get(URL)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "lxml")

with open('music_title_list_from_karatetsu.csv', 'w', newline='') as f:
    for title in soup.find_all("a", class_="pclink", target="_blank"):
        writer = csv.writer(f)
        # 曲についている不要な括弧をそれごと削除 ex. (TV ver)
        only_music_title = re.sub(r'（.+?）', '', title.text)
        writer.writerow([only_music_title])
