# 指定したpathが絶対パスか相対パスかを判定(os.path.isabs)
# pathが絶対パスならTure、相対パスならFalseを返す

import os

path = './test/sub1/a.txt'
print(os.path.isabs(path))

# 実行結果
# False