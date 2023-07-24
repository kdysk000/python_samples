# GETメソッド (戻り値がJSONデータの場合の処理方法)
#
# WEBから取得するJSONデータにはUnicodeエスケープシーケンス(\uで始まる)などの文字列が含まれているため
# 下記のメソッドを使って辞書型もしくは辞書のリストに変換が必要
#
# requests.json()
# 
# レスポンスがJSONかどうかはレスポンスヘッダのContent-Typeで確認する
#

import requests

url    = 'https://api.bitflyer.com/v1/ticker'
params = {'product_code': 'btc_jpy'}

r = requests.get(url, params=params)

# Content-Typeを確認しJSONなら変換
if 'application/json' in r.headers['Content-Type'] :
    print(r.json())