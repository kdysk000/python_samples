# 1次元配列を多次元配列に変換 (reshape)
# reshape( 行数, 列数 )

import numpy as np

ar = np.array([1,2,3,4,5,6])
ar =ar.reshape( 2, 3 )
print(ar)