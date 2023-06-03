# Seriesへのデータの追加

import pandas as pd

ser = pd.Series( data = [ 1,2,3 ], index = [ 'a', 'b', 'c' ], name = 'X' )
print(ser)
print()

ser['d'] = 4
print(ser)