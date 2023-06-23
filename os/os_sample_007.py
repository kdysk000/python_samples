# 指定されたパスのファイル名のみを取得する(os.path.basename)

import os

path = './test/sub1/a.txt'
print(os.path.basename(path))

# 実行結果
# a.txt