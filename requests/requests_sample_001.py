# GETメソッド (requests.get)
#
# response = requests.get(URL, その他任意の引数)
# 引数
#   URL     : 読み込み対象のURL
#   headers : ヘッダとして送信する内容を辞書で指定
#   timeout : クエストのタイムアウト時間
#   params  : URLのクエリパラメータを辞書で指定
#   cookies : クッキーとして送信する内容を辞書で指定
#
# 戻り値
#   response (requests.models.Response)
#     status_code : ステータスコード
#     headers     : レスポンスヘッダの内容
#     content     : レスポンスのバイナリデータ
#     text        : レスポンスの内容
#     encoding    : エンコーディング
#     elapsed     : レスポンスタイム
#     cookies     : クッキー

import requests

url = "https://google.com"
r = requests.get(url)

print(r.status_code)
# print(r.headers)
print(r.headers['Content-Type'])
# print(r.content)
# print(r.text)
# print(r.encoding)
# print(r.cookies)
# print(r.elapsed)
