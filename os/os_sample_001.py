# ファイルやディレクトリの一覧を取得(os.work)

import os
 
for curDir, dirs, files in os.walk("test"):
    print('===================')
    print("カレントディレクトリ: " + str(curDir))
    print("サブディレクトリ:" + str(dirs))
    print("内包するファイル: " + str(files))