# DataFrameへの列の追加 (assign)
# 注：新たなオブジェクトが返され、元のオブジェクトは変更されない

import pandas as pd

df =pd.DataFrame( data = [[1,2,3],[4,5,6],[7,8,9]], index = [ 'a', 'b', 'c' ], columns = [ 'A', 'B', 'C' ] )
print(df)
print()

df.assign(D=0) #元のオブジェクトは変更されない
print(df)
print()

df = df.assign(D=0)
print(df)