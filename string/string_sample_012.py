# 特定のフレーズで始まっているかの判定(endswith)
#
# endswith(suffix)
#   文字列がsuffixで指定されたフレーズで終わっていればTrue、そうでなければFalseを返す

str = 'this is a pen'

print(str.endswith('this'))
print(str.endswith('pen'))

# 実行結果
# False
# True