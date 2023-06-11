# 辞書から任意の要素を取り出し削除する (popitem)
# 戻り値としてキーと値のタプルが返る

test_results = { 'japanese':90, 'math':88, 'english':79, 'science':81, 'society':93, 'chinese':70 }

test_result = test_results.popitem()
print(test_result)
print(test_results)
