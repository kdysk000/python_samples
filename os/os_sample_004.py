# ファイル・ディレクトリの存在確認(os.path.exists)
# 存在すればTrue、存在しなければFalseを返す

import os

path = './test/sub1/'
print(os.path.exists(path))

path = './test/sub1/z.txt'
print(os.path.exists(path))

# 実行結果
# True
# False