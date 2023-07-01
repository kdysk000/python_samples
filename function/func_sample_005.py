# 複数のキーワード引数をまとめて辞書に変換して受け取る
# def 関数名(**kwargs):
#     処理
#     return 戻り値
#
# キーワード引数：どの引数の値なのかを日キッス名で指定する

def test(**kwargs):
    print(type(kwargs))
    print(kwargs)

test(apple=1, orange=2, banana=3)


# 実行結果
# <class 'dict'>
# {'apple': 1, 'orange': 2, 'banana': 3}