# 既存の辞書に値を追加や削除する場合、指定のキーの値があるかどうかで結果が変わる
# キーがあれば更新され、なければ追加

test_results = { 'japanese':90, 'math':88, 'english':79, 'science':81, 'society':93 }

# mathはすでにあるので更新
test_results['math'] = 89
print(test_results)

#chineseはないので追加
test_results['chinese'] = 70
print(test_results)


# 実行結果
# {'japanese': 90, 'math': 89, 'english': 79, 'science': 81, 'society': 93}
# {'japanese': 90, 'math': 89, 'english': 79, 'science': 81, 'society': 93, 'chinese': 70}