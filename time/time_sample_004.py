# 処理を一時的に停止する (time.sleep)
# sleep(秒) : 指定された秒だけ処理を待機

import time

# sleep前の時刻
t1 = time.ctime() 

# 1秒停止 
time.sleep(1)
 
# sleep後の時刻
t2 = time.ctime()
 
print(f"sleep前時間：{t1}")
print(f"sleep後時間：{t2}")


# 実行結果
# sleep前時間：Tue Jun 27 22:03:44 2023
# sleep後時間：Tue Jun 27 22:03:45 2023