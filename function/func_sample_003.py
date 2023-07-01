# デフォルト引数がある関数の定義
# def 関数名( 引数1, 引数2=初期値, ... 引数n=初期値 ):
#     処理
#     return 戻り値

def add(a, b=10):
    return a + b

ret = add(3, 5)
print(ret)

ret = add(3)  # 第2引数の指定なしのため初期値が使用される
print(ret)


# 実行結果
# 8
# 13