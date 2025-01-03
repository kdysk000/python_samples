# try  :
#     例外が発生する可能性がある処理
# except 例外1:
#     例外1を受けて実行する処理
# except 例外2:
#     例外2を受けて実行する処理
# except :
#     例外1と2以外の例外を受けた場合に実行する処理

num = "a"

try :
    ret = 1000 / int(num)
    print(ret)
except ValueError:
    print("Value Error.")
except ZeroDivisionError:
    print("Zero Division Error.")
except :
    print("Other Error.")

num = 0

try :
    ret = 1000 / int(num)
    print(ret)
except ValueError:
    print("Value Error.")
except ZeroDivisionError:
    print("Zero Division Error.")
except :
    print("Other Error.")

# 実行結果
# Value Error.
# Zero Division Error.