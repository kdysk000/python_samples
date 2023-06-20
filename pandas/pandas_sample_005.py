# Seriesのデータ削除 (drop)
# pd.Series (data=データの配列, index=インデックスの配列, name=列名)

import pandas as pd

ser = pd.Series( data = [ 1,2,3 ], index = [ 'a', 'b', 'c' ], name = 'X' )
print(ser)
print()

ser = ser.drop('c')
print(ser)


# 実行結果
# a    1
# b    2
# c    3
# Name: X, dtype: int64
# 
# a    1
# b    2
# Name: X, dtype: int64