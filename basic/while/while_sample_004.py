# while 条件式 :
#     処理A    条件式が True の間、繰り返し実行される
# else :
#     処理B    while文を抜ける前に実行される
#

count = 1
while count <=5 :
    print(count)
    count += 1
else :
    print("finish while loop.")

# 実行結果
# 1
# 2
# 3
# 4
# 5
# finish while loop.