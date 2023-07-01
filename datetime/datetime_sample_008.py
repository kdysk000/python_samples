# 任意のフォーマットの日時文字列からdatetimeオブジェクトを作成 (datetime.datetime.strptime)
# datetime.datetime.strptime(文字列, フォーマット)

import datetime

str = '2023/12/31 23:59:59'
dt = datetime.datetime.strptime(str, '%Y/%m/%d %H:%M:%S')
print(dt)


# 実行結果
# 2023-12-31 23:59:59