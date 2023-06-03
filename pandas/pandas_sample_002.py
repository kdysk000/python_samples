# DataFrameの作成
# pd.DataFrame (data=データの配列, index=インデックスの配列, columns=列名の配列)

import pandas as pd
import numpy as np

# リストからの作成
df =pd.DataFrame( data = [[1,2,3],[4,5,6],[7,8,9]], index = [ 'a', 'b', 'c' ], columns = [ 'X', 'Y', 'Z' ] )
print(df)
print()

# 複数の1次元配列からの作成
df = pd.DataFrame( {
        'X' : pd.Series( data = [ 1, 4, 7 ], index = [ 'a', 'b', 'c' ] ),
        'Y' : pd.Series( data = [ 2, 5, 8 ], index = [ 'a', 'b', 'c' ] ),
        'Z' : pd.Series( data = [ 3, 6, 9 ], index = [ 'a', 'b', 'c' ] )
} )
print(df)
print()

# 辞書(dict)からの作成
df = pd.DataFrame( [
    { 'X': 1, 'Y': 2, 'Z': 3},
    { 'X': 4, 'Y': 5, 'Z': 6},
    { 'X': 7, 'Y': 8, 'Z': 9} ], index = [ 'a', 'b', 'c' ] )
print(df)
print()

# NumPyからの作成
df =pd.DataFrame( data = np.array([[1,2,3],[4,5,6],[7,8,9]]), index = [ 'a', 'b', 'c' ], columns = [ 'X', 'Y', 'Z' ] )
print(df)
