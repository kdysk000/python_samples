# 特定のフレーズで始まっているかの判定(startswith)
#
# startswith(prefix)
#   文字列がprefixで指定されたフレーズで始まっていればTrue、そうでなければFalseを返す

str = 'this is a pen'

print(str.startswith('this'))
print(str.startswith('pen'))

# 実行結果
# True
# False