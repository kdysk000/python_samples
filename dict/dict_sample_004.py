# キーと値のリストから辞書を作成
# zip()を利用

subjects = [ 'japanese', 'math', 'english', 'science', 'society' ]
points = [ 90, 88, 79, 81, 93 ]

test_results = dict(zip(subjects, points))
print(test_results)
