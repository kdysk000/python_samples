# JSON文字列をPythonオブジェクトに変換 (json.loads)
# json.loads(文字列)
# 戻り値はdict型

import json

str = '{"persons": [{"id": 1, "name": "hoge", "age": 25}, {"id": 2, "name": "fuga", "age": 40}]}'
d = json.loads(str)

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