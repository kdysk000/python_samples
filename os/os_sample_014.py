# 環境変数の取得・設定(os.environ)

import os

print(os.environ["HOME"])

# os.environ.get()で取得する場合
print(os.environ.get("HOME"))

# 新しい環境変数を設定
os.environ["HOGEHOGE"] = "hogehoge"
print(os.environ.get("HOGEHOGE"))

# 実行結果
# /home/hoge
# /home/hoge
# hogehoge