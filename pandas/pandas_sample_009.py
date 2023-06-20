# DataFrameへの列の追加 (insert)
# insert (位置, 列名, データ)

import pandas as pd

df =pd.DataFrame( data = [[2,3],[5,6],[8,9]], index = [ 'a', 'b', 'c' ], columns = [ 'B', 'C' ] )
print(df)
print()

df.insert(0, 'A', [ 1, 4, 7 ])
print(df)


# 実行結果
#    B  C
# a  2  3
# b  5  6
# c  8  9
# 
#    A  B  C
# a  1  2  3
# b  4  5  6
# c  7  8  9