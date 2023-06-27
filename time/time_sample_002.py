# 時刻の文字列をオブジェクト(time.struct_time)に変換 (time.strptime)
# strptime(string[, format]) : 時刻を表す文字列を書式に従って解釈する
# 戻り値はstruct_time型

import time

now = time.ctime()
cnvtime = time.strptime(now)

print(type(cnvtime))
print(cnvtime)

str = '2023/06/27 21:36:00'
cnvtime = time.strptime(str, '%Y/%m/%d %H:%M:%S')

print(cnvtime)

# 実行結果
# <class 'time.struct_time'>
# time.struct_time(tm_year=2023, tm_mon=6, tm_mday=27, tm_hour=21, tm_min=34, tm_sec=42, tm_wday=1, tm_yday=178, tm_isdst=-1)
# time.struct_time(tm_year=2023, tm_mon=6, tm_mday=27, tm_hour=21, tm_min=36, tm_sec=0, tm_wday=1, tm_yday=178, tm_isdst=-1)