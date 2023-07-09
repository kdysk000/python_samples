# 初期化メソッドを定義する
#
# 初期化メソッド
# def __init__(self, 引数1, 引数2, ... 引数n):
#     初期化処理
#
# インスタンス変数の初期化
# self.変数名 = 初期値

class Car:
    # 初期化メソッド
    def __init__(self, color = "white"):
        self.color = color
        print("color is", color)

car1 = Car()  # インスタンス作成 (引数なしなので初期値)
car2 = Car("black")  # インスタンス作成 (引数あり)


# 実行結果
# color is white
# color is black