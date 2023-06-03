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