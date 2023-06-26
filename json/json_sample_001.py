# JSONファイルをPythonオブジェクトとして読み込む (json.load)
# json.load(ファイルオブジェクト)
# 戻り値はdict型

import json

with open('./data/sample.json', 'r') as f:
    d = json.load(f)

print(type(d))
print(d)
print(d['persons'][0])
print(d['persons'][1])
print(d['persons'][0]['name'])
print(d['persons'][1]['name'])


# 実行結果
# <class 'dict'>
# {'persons': [{'id': 1, 'name': 'hoge', 'age': 25}, {'id': 2, 'name': 'fuga', 'age': 40}]}
# {'id': 1, 'name': 'hoge', 'age': 25}
# {'id': 2, 'name': 'fuga', 'age': 40}
# hoge
# fuga