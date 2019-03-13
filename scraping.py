# 曲のタイトルデータを取得して、ファイルに落としてくれるプログラム

import requests
import csv
from bs4 import BeautifulSoup

URL = 'https://www.karatetsu.com/animegame/pickup/ranking.php'

response = requests.get(URL)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "lxml")

for title in soup.find_all("a", class_="pclink", target="_blank"):
    print(title.text)

# print(soup)
