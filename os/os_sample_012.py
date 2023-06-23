# 引数で指定したパスの絶対パスを返す(os.path.abspath)

import os

path = os.path.abspath('./test/sub1/a.txt')
print(path)

# 実行結果
# /home/hoge/work/python_samples/os/test/sub1/a.txt