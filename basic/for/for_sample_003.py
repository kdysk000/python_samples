# for 変数 in オブジェクト :
#     処理A    オブジェクトの値を全て取り出すまで繰り返す
# else :
#     処理B    繰り返しが正常に完了したら実行(途中で break した場合は実行されない)
#

colors = [ "blue", "red", "green", "yellow" ]

for name in colors :
    print(name)
else :
    print("finish for loop.")

for name in colors :
    if name == "green" :
        break
    print(name)
else :
    print("finish for loop.")    # 途中で break するので実行されない

# 実行結果
# blue
# red
# green
# yellow
# finish for loop.
#
# blue
# red
