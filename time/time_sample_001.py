# 時刻の取得 (time.time、time.gmtime、time.ctime)
# time() : システム時刻(UNIXタイム)の取得
# 戻り値はfloat型
# ※ UNIX時間は、1970年1月1日0時0分0秒を基準とし基準から何秒経っているかを表す時刻
#
# gmtime(secs) :
# エポックからの経過時間で表現された時刻の取得
# 引数指定なしの場合は現在の時刻
# 戻り値はtime.struct_time型
#
# ctime(secs) : 
# エポックからの経過秒数で表現された時刻の取得
# 引数指定なしの場合は現在の時刻
# 戻り値は文字列

import time

print(type(time.time()))
print(time.time())

print("---")
print(type(time.gmtime()))
print(time.gmtime())

print("---")
print(type(time.ctime()))
str = time.ctime()
print(str)


# 実行結果
# <class 'float'>
# 1687785324.9061937
# ---
# <class 'time.struct_time'>
# time.struct_time(tm_year=2023, tm_mon=6, tm_mday=26, tm_hour=13, tm_min=15, tm_sec=24, tm_wday=0, tm_yday=177, tm_isdst=0)
# ---
# <class 'str'>
# Mon Jun 26 22:15:24 2023