# 現在の日付を取得 (datetime.date.today)
# 戻り値はdatetime.date型

import datetime

today = datetime.date.today()

print(type(today))
print(today)
print(today.year)
print(today.month)
print(today.day)


# 実行結果
# <class 'datetime.date'>
# 2023-07-01
# 2023
# 7
# 1