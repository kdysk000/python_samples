# ファイルやディレクトリの一覧を取得(os.listdir)

import os
 
path1 = './test'
path2 = './test/sub1'
 
dir = os.listdir(path1)
print(dir)

dir = os.listdir(path2)
print(dir)

# 実行結果
# ['sub3', 'sub2', 'sub1']
# ['c.txt', 'a.txt', 'b.txt']