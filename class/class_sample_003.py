# インスタンスメソッドを定義する
#
# 初期化メソッド
# def メソッド名(self, 引数1, 引数2, ... 引数n):
#     ステートメント
#
# インスタンスメソッドの実行
# インスタンス.メソッド()

class Car:
    # 初期化メソッド
    def __init__(self, color = "white"):
        self.color = color
        print("initial color is", color)

    # インスタンスメソッド
    def setColor(self, color):
        self.color = color
        print("set color is", color)

car = Car()  # インスタンス作成 (引数なしなので初期値)
car.setColor("red")  # インスタンスメソッド実行


# 実行結果
# initial color is white
# set color is red