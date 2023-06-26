# PythonオブジェクトをJSON文字列として整形して出力 (json.dump)
# json.dumps(dictなどのオブジェクト)
# 戻り値は文字列

import json
import os

path = 'data/test.json'

d = {
    "persons": [
        {"id": 1, "name": "hoge", "age": 25},
        {"id": 2, "name": "fuga", "age": 40}
    ]
}

str = json.dumps(d, indent=2)
print(str)


# 実行結果
# {
#   "persons": [
#     {
#       "id": 1,
#       "name": "hoge",
#       "age": 25
#     },
#     {
#       "id": 2,
#       "name": "fuga",
#       "age": 40
#     }
#   ]
# }