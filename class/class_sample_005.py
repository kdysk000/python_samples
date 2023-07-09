# クラスメソッドを定義する
# 
# @classmethod
# def メソッド名(cls, 引数1, 引数2, ... 引数n):
#     ステートメント

class Car:
    # クラス変数
    maker = "TOYOTA"
    count = 0

    # クラスメソッド
    @classmethod
    def countup(cls):
        cls.count += 1

    # 初期化メソッド
    def __init__(self, color = "white"):
        self.color = color
        Car.countup()
        print("color is", color)

car1 = Car()  # インスタンス作成
print("count is", Car.count)

car2 = Car("red")  # インスタンス作成
print("count is", Car.count)


# 実行結果
# color is white
# count is 1
# color is red
# count is 2