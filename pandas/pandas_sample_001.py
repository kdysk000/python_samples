# Seriesの作成
# pd.Series (data=データの配列, index=インデックスの配列, name=列名)

import pandas as pd
import numpy as np

# リストからの作成
ser = pd.Series( data = [ 1,2,3,4 ], index = [ 'a', 'b', 'c', 'd' ], name = 'X' )
print(ser)

# 辞書(dict)からの作成
ser  = pd.Series( data = dict(a=1, b=2, c=3, d=4 ), name = 'X' )
print(ser)

# NumPyからの作成
ser  = pd.Series( data = np.array([1,2,3,4]), index = [ 'a', 'b', 'c', 'd' ], name = 'X' )
print(ser)
