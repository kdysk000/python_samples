# Seriesのデータ削除 (drop)
# pd.Series (data=データの配列, index=インデックスの配列, name=列名)

import pandas as pd

ser = pd.Series( data = [ 1,2,3 ], index = [ 'a', 'b', 'c' ], name = 'X' )
print(ser)
print()

ser = ser.drop('c')
print(ser)
