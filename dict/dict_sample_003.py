# 初期値で辞書を作成 (dict.formkeys)
# dict.formkeys( イテレータ, 初期値 )

test_results = dict.fromkeys(['japanese', 'math', 'english', 'science', 'society'], 0)
print(test_results)


# 実行結果
# {'japanese': 0, 'math': 0, 'english': 0, 'science': 0, 'society': 0}