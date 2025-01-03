# try  :
#     例外が発生する可能性がある処理
# except :
#     例外を受けて実行する処理
# finally :
#     try 文を抜ける前に実行する処理

num = "a"

try :
    price = 120 * int(num)
    print("金額:", price)
except :
    print("error.")
finally :
    print("finish try.")    # 例外が発生してもしなくても最後に実行される

# 実行結果
# error.
# finish try.