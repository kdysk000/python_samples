# ファイルの存在確認(os.path.isfile)
# 存在すればTrue、存在しなければFalseを返す
# ファイルではない場合もFalseを返す

import os

path = './test/sub1'
print(os.path.isfile(path))

path = './test/sub1/a.txt'
print(os.path.isfile(path))

# 実行結果
# False
# True