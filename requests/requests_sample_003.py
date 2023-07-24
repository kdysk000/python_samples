# GETメソッド (取得したデータ(ZIPなど)をファイルとして保存する場合)
#
# response.contentにバイナリデータが保存されているのでこれをファイルに書き出す
#

import requests

# 下記URL先は、市町村情報が記載されているCSVを、ZIPファイルで、提供している。
url = 'http://zipcloud.ibsnet.co.jp/zipcodedata/download?di=1661933424166'

r = requests.get(url)

# 下記メソッドの第一引数は、ファイルパスを指定
with open('./out/sample_003.zip', 'wb') as f:
    f.write(r.content)
