# ループカウンタ付きで全ての要素を順に取り出す (enumerate)
# for i, j in enumerate(リスト, 開始値 ):
# 開始値を省略した場合は0

words = [ 'apple', 'banana', 'orrange', 'peach' ]

for i, word in enumerate(words):
    print( i, word )


# 実行結果
# 0 apple
# 1 banana
# 2 orrange
# 3 peach