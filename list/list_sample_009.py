# リストの複製 (copy)
# copy()

li1 = [1, 2, 3, 4]
li2 = li1         # li1とli2は同じオブジェクトの参照
li3 = li1.copy()  # li3は別オブジェクトとして新しく作成

print(li2)
print(li1 is li2)

print(li2)
print(li1 is li3)


# 実行結果
# [1, 2, 3, 4]
# True
# [1, 2, 3, 4]
# False