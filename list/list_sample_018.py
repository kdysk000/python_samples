# リストに値が含まれているかの判定
# in演算子を使い「値 in リスト」で判定でき値が含まれていればTrueを返す

nums = [ 1, 2, 3, 4, 5 ]

if 1 in nums:
    print( "1 in nums" )
else:
    print( "1 not in nums" )

if 6 in nums:
    print( "6 in nums" )
else:
    print( "6 not in nums" )


# 実行結果
# 1 in nums
# 6 not in nums