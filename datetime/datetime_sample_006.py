# 日時の足し算、引き算(datetime.timedelta)
# datetime.timedelta( days=0 , seconds=0 , microseconds=0 , milliseconds=0 , minutes=0 , hours=0 , weeks=0 )

import datetime

now = datetime.datetime.now()
today = datetime.date.today()
td = datetime.timedelta(days = 2)

print(now + td)
print(now - td)

print(today + td)
print(today - td)


# 実行結果
# 2023-07-03 16:56:16.663788
# 2023-06-29 16:56:16.663788
# 2023-07-03
# 2023-06-29