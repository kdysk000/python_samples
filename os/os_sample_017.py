# ファイル名,ディレクトリ名の変更(os.rename)
# os.rename(変更前ファイル、変更後ファイル)

import os

before = './test/sub4'
after = './test/sub5'
os.rename(before, after)