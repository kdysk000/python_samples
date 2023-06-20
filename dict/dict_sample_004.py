# キーと値のリストから辞書を作成
# zip()を利用

subjects = [ 'japanese', 'math', 'english', 'science', 'society' ]
points = [ 90, 88, 79, 81, 93 ]

test_results = dict(zip(subjects, points))
print(test_results)


# 実行結果
# {'japanese': 90, 'math': 88, 'english': 79, 'science': 81, 'society': 93}