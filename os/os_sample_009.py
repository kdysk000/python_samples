# 指定されたパスのファイル名とそれまでのパスを取得する(os.path.split)

import os

path = './test/sub1/a.txt'
dir, file = os.path.split(path)
print(dir)
print(file)

# 実行結果
# ./test/sub1
# a.txt