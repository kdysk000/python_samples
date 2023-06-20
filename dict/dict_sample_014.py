# 辞書の全ての値を取り出しリスト化 (values)

test_results = { 'japanese':90, 'math':88, 'english':79, 'science':81, 'society':93 }

points = list(test_results.values())
print(points)


# 実行結果
# [90, 88, 79, 81, 93]