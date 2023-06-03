# DataFrameへの列の追加 (insert)
# insert (位置, 列名, データ)

import pandas as pd

df =pd.DataFrame( data = [[2,3],[5,6],[8,9]], index = [ 'a', 'b', 'c' ], columns = [ 'B', 'C' ] )
print(df)
print()

df.insert(0, 'A', [ 1, 4, 7 ])
print(df)