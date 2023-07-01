# 現在の日時を取得 (datetime.datetime.now)
# 戻り値はdatetime.datetime型

import datetime

now = datetime.datetime.now()

print(type(now))
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)


# 実行結果
# <class 'datetime.datetime'>
# 2023-07-01 16:14:10.015821
# 2023
# 7
# 1
# 16
# 14
# 10
# 15821
