# 処理時間を計測する (time.perf_counter)
# 単位は秒
# time.time()より高精度で時間を計測できる

import time

# 処理前の時刻
t1 = time.perf_counter() 
 
# 計測したい処理
for i in range(1000000):
    i ** 10
 
# 処理後の時刻
t2 = time.perf_counter()
 
# 経過時間を表示
elapsed_time = t2-t1
print(f"経過時間：{elapsed_time}")


# 実行結果
# 経過時間：0.34447216987609863