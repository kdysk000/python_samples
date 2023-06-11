# 条件式付きリスト内包表記
# [ 式 for 変数 in イテラブル if 条件式 ]

nums = [ 1, 4, 2, 3, 5 ]
double_nums = [ num*2 for num in nums if num > 2 ]  # 3以上の数値だけ取り出す
print( double_nums )