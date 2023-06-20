# 範囲から配列を作成 (arange)
# np.arange( start, stop, step, dtype=None )

import numpy as np

ar1 = np.arange( 0, 10 )
print( ar1 )

ar2 = np.arange( 0, 20, 2 )
print( ar2 )


# 実行結果
# [0 1 2 3 4 5 6 7 8 9]
# [0 2 4 6 8 10 12 14 16 18]