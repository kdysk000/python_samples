# ソートで使う比較関数を指定する
# sort()およびsortedは大きさを比較する際に使用する比較関数を指定可能
#
# sort( key = 関数名 )
# sorted( リスト, key = 関数名 )

words = [ 'ab', 'c', 'defg', 'hij']
print(words)

words.sort( key=len )
print(words)


# 実行結果
# ['ab', 'c', 'defg', 'hij']
# ['c', 'ab', 'hij', 'defg']