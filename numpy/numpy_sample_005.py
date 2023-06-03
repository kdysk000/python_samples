# 要素の追加 (append)
# np.append( 配列, 値, axis = None )
# np.append( 配列, リスト, axis = None )
# np.append( 配列, タプル, axis = None )
# axis：0:行を追加、1:列を追加

import numpy as np

ar1 = np.array([1,2,3,4,5,6])
ar1 = ar1.reshape( 2, 3 )

ar2 = np.array([7,8,9,10,11,12])
ar2 = ar2.reshape( 2, 3 )

print( np.append(ar1, ar2, axis=0) )
print( np.append(ar1, ar2, axis=1) )