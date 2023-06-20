# 要素の挿入 (insert)
# np.insert( 配列, 位置, 値, axis = None )
# np.insert( 配列, 位置, リスト, axis = None )
# np.insert( 配列, 位置, タプル, axis = None )
# axis：0:行を追加、1:列を追加

import numpy as np

ar1 = np.array([1,2,3,4,5,6])
ar1 = ar1.reshape( 2, 3 )

ar2 = np.array([7,8,9])

print( np.insert(ar1, 1, ar2, axis=0) )
print( np.insert(ar1, 1, 0, axis=1) )


# 実行結果
# [[1 2 3]
#  [7 8 9]
#  [4 5 6]]
# [[1 0 2 3]
#  [4 0 5 6]]