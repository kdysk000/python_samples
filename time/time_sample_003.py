# 時刻を指定したフォーマットで文字列に変換 (time.strftime)
# strftime(format[, t] : tの指定なしの場合、localtime() が返す値を現在の時刻として使用される
# 戻り値は文字列

import time

now = time.gmtime()
str = time.strftime('%Y/%m/%d %H:%M:%S', now)

print(type(str))
print(str)


# 実行結果
# <class 'str'>
# 2023/06/27 12:50:04