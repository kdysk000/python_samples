# 指定したディレクトリを削除(os.rmdir)
# ディレクトリが空でない場合はエラー

import os

dir = './test/sample_018'

if os.path.exists(dir):
    os.rmdir(dir)