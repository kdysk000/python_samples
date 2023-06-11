# 辞書にキーが存在しているか調べる
# in演算子を利用

test_results = { 'japanese':90, 'math':88, 'english':79, 'science':81, 'society':93 }

if 'math' in test_results:
    print("math is exist in dict")
else:
    print("math is not exist in dict")

if 'chinese' in test_results:
    print("chinese is exist in dict")
else:
    print("chinese is not exist in dict")
