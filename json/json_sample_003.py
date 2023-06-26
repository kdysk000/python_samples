# PythonオブジェクトをJSONファイルとして保存 (json.dump)
# json.dump(dictなどのオブジェクト, ファイルオブジェクト, indentなど)

import json
import os

path = 'data/test.json'

d = {
    "persons": [
        {"id": 1, "name": "hoge", "age": 25},
        {"id": 2, "name": "fuga", "age": 40}
    ]
}

# data/test.jsonが存在すれば削除
if os.path.isfile(path):
    os.remove(path)

with open(path, 'w') as f:
    json.dump(d, f, indent=2)