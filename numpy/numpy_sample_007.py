# 要素の削除 (delete)
# np.delete( 配列, obj, axis = None )
# obj：削除する行番号や列番号を整数、スライス、リストで指定
# axis：0:行を追加、1:列を追加

import numpy as np

ar = np.array([1,2,3,4,5,6])
ar = ar.reshape( 2, 3 )

print( np.delete(ar, 1, axis=0) )
print( np.delete(ar, 1, axis=1) )


# 実行結果
# [[1 2 3]]
# [[1 3]
#  [4 6]]