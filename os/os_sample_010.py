# 指定されたパスの拡張子とそれまでのパスを取得する(os.path.splitext)

import os

path = './test/sub1/a.txt'
dir, file = os.path.splitext(path)
print(dir)
print(file)

# 実行結果
# ./test/sub1/a
# .txt