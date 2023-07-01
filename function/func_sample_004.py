# 可変長引数がある関数の定義
# def 関数名(*args):
#     処理
#     return 戻り値
#
# argsには引数に渡された値がタプルにまとめて入る

def add(*args):
    return sum(args)

ret = add(1,2)
print(ret)

ret = add(1,2,3)
print(ret)


# 実行結果
# 3
# 6