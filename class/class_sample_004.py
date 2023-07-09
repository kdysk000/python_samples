# クラス変数を定義する
# クラス変数は全てのインスタンスで共有される

class Car:
    # クラス変数
    maker = "TOYOTA"

    # 初期化メソッド
    def __init__(self, color = "white"):
        self.color = color
        print("color is", color)

car = Car()  # インスタンス作成
print("maker is", Car.maker)


# 実行結果
# color is white
# maker is TOYOTA