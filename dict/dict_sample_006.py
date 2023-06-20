# 他の辞書で更新 (update)
# 同じキーがあれば更新され、なければ追加

test_results = { 'japanese':90, 'math':88, 'english':79, 'science':81,  'society':93 }
new_results = { 'japanese':91, 'chinese':70 }

test_results.update(new_results)
print(test_results)


# 実行結果
# {'japanese': 91, 'math': 88, 'english': 79, 'science': 81, 'society': 93, 'chinese': 70}