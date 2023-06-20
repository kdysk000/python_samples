# DataFrameへの列の追加 (assign)
# 注：新たなオブジェクトが返され、元のオブジェクトは変更されない

import pandas as pd

df =pd.DataFrame( data = [[1,2,3],[4,5,6],[7,8,9]], index = [ 'a', 'b', 'c' ], columns = [ 'A', 'B', 'C' ] )
print(df)
print()

df.assign(D=0) #元のオブジェクトは変更されない
print(df)
print()

df = df.assign(D=0)
print(df)


# 実行結果
#    A  B  C
# a  1  2  3
# b  4  5  6
# c  7  8  9
# 
#    A  B  C
# a  1  2  3
# b  4  5  6
# c  7  8  9
# 
#    A  B  C  D
# a  1  2  3  0
# b  4  5  6  0
# c  7  8  9  0