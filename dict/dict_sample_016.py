# 辞書から指定したキーの値を取り出し削除する (pop)
# 指定したキーがなければKeyError

test_results = { 'japanese':90, 'math':88, 'english':79, 'science':81, 'society':93, 'chinese':70 }

point = test_results.pop('chinese')
print(point)
print(test_results)
