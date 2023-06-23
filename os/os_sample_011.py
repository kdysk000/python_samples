# 引数で指定された2つの文字列を結合(os.path.join)

import os

path = './test/sub1'
file = 'a.txt'
fullpath = os.path.join(path, file)
print(fullpath)

# 実行結果
# ./test/sub1/a.txt