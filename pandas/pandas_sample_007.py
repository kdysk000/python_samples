# DataFrameへの列の追加
# 新規列名を指定

import pandas as pd

df =pd.DataFrame( data = [[1,2,3],[4,5,6],[7,8,9]], index = [ 'a', 'b', 'c' ], columns = [ 'A', 'B', 'C' ] )
print(df)
print()

df['D'] = 0
print(df)
print()

df['E'] = [ 0, 1, 2 ]
print(df)


# 実行結果
#    A  B  C
# a  1  2  3
# b  4  5  6
# c  7  8  9
# 
#    A  B  C  D
# a  1  2  3  0
# b  4  5  6  0
# c  7  8  9  0
# 
#    A  B  C  D  E
# a  1  2  3  0  0
# b  4  5  6  0  1
# c  7  8  9  0  2