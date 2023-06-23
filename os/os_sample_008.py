# 指定されたパスからファイル名を除いたものを取得する(os.path.dirname)

import os

path = './test/sub1/a.txt'
print(os.path.dirname(path))

# 実行結果
# ./test/sub1