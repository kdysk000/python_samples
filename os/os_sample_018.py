# 指定したファイルを削除(os.remove)

import os

dir = './test/sample_018'
path = './test/sample_018/test.txt'

# ディレクトリ作成
if not os.path.exists(dir):
    os.mkdir(dir)

# 作成したディレクトリにファイル作成
os.system('touch ./test/sample_018/test.txt')

# ファイルの存在確認
print(os.path.isfile(path))

# ファイル削除
os.remove(path)

# ファイルの存在確認
print(os.path.isfile(path))

# 実行結果
# True
# False