# DataFrameの値を抽出(単独要素 or 複数要素)(loc)
# loc[ index名, 列名 ]

import pandas as pd

df =pd.DataFrame( data = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], index = [ 'a', 'b', 'c', 'd' ], columns = [ 'A', 'B', 'C', 'D' ] )
print(df)
print()

print(df.loc['a':'c', ['A', 'C']])


# 実行結果
#     A   B   C   D
# a   1   2   3   4
# b   5   6   7   8
# c   9  10  11  12
# d  13  14  15  16
# 
#    A   C
# a  1   3
# b  5   7
# c  9  11