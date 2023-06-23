# ディレクトリの存在確認(os.path.isdir)
# 存在すればTrue、存在しなければFalseを返す
# ディレクトではない場合もFalseを返す

import os

path = './test/sub1'
print(os.path.isdir(path))

path = './test/sub1/a.txt'
print(os.path.isdir(path))

# 実行結果
# True
# False