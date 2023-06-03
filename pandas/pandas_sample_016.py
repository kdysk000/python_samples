# 値の抽出(単独要素 or 複数要素)
# iloc[ 行番号, 列番号 ]

import pandas as pd

df =pd.DataFrame( data = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], index = [ 'a', 'b', 'c', 'd' ], columns = [ 'A', 'B', 'C', 'D' ] )
print(df)
print()

print(df.iloc[0:3, [0, 2]])