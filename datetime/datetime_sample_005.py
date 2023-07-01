# 任意の時刻のtimeオブジェクトを作成 (datetime.time)

import datetime

t = datetime.time (12 , 30 , 20 , 1230)

print(type(t))
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

# 実行結果
# <class 'datetime.time'>
# 12:30:20.001230
# 12
# 30
# 20
# 1230