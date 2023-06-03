# DataFrameへの列の追加 (append)
# append( 追加する行データ )
# 注：将来的に削除予定のメソッド。concat()の使用を推奨

import pandas as pd

df1 =pd.DataFrame( data = [[1,2,3,4],[5,6,7,8]], index = [ 'a', 'b' ], columns = [ 'A', 'B', 'C', 'D' ] )
print(df1)

df2 =pd.DataFrame( data = [[9,10,11,12],[13,14,15,16]], index = [ 'c', 'd' ], columns = [ 'A', 'B', 'C', 'D' ] )
print(df2)

df3 = df1.append(df2)
print(df3)