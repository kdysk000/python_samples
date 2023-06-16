# 辞書にキーが存在しているか調べる
# in演算子を利用
# 存在しないことを確認する場合はnot in

test_results = { 'japanese':90, 'math':88, 'english':79, 'science':81, 'society':93 }

# あればTrue
if 'math' in test_results:
    print("math is exist in dict")
else:
    print("math is not exist in dict")

# なければTrue
if 'chinese' not in test_results:
    print("chinese is not exist in dict")
else:
    print("chinese is exist in dict")
