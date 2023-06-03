# ソート (sort)
# sort()        元の配列を並べ替える
# sort( 配列 )  ソート済みの新しい配列を返す

import numpy as np

ar0 = np.array([9,2,6,1,0,4,3,8,5,7])
ar1 = ar0.copy()    #配列のコピー

ar1.sort()            # 元の配列ar1をソート
print( ar1 )

ar2 = np.sort( ar0 )  # 元の配列ar0はソートされない
print( ar2 )
print( ar0 )