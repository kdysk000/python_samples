# 任意の日付のdateオブジェクトを作成 (datetime.date)
# datetime.date(year , month , day)  ※ 全て必須
# 戻り値はdatetime.date型

import datetime

d = datetime.date(2023, 12, 31)

print(d)
print(d.year)
print(d.month)
print(d.day)


# 実行結果
# 2023-12-31
# 2023
# 12
# 31