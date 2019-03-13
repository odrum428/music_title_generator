# 曲のタイトルデータを取得して、ファイルに落としてくれるプログラム

import requests

URL = 'https://www.karatetsu.com/animegame/pickup/ranking.php'

response = requests.get(URL)
response.encoding = response.apparent_encoding
print(response.text)
