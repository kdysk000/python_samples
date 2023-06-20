# DataFrameの連結 (concat)
# pd.concat(連結するオブジェクト, axis=0/1, join='inner'/'outer')
# axis：0 縦方向(行)、1 横方向(列) (defaultは0)
# join：'inner' 内部結合、'outer' 外部結合(defaultは'outer')

import pandas as pd

df1 =pd.DataFrame( data = [[1,2],[5,6],[9,10]], index = [ 'a', 'b', 'c' ], columns = [ 'A', 'B' ] )
print(df1)
print()

df2 =pd.DataFrame( data = [[3,4],[7,8],[11,12]], index = [ 'a', 'b', 'c' ], columns = [ 'C', 'D' ] )
print(df2)
print()

df3 = pd.concat( [df1, df2], axis=0 )
print(df3)
print()

df4 = pd.concat( [df1, df2], axis=1 )
print(df4)


# 実行結果
#    A   B
# a  1   2
# b  5   6
# c  9  10
# 
#     C   D
# a   3   4
# b   7   8
# c  11  12
# 
#      A     B     C     D
# a  1.0   2.0   NaN   NaN
# b  5.0   6.0   NaN   NaN
# c  9.0  10.0   NaN   NaN
# a  NaN   NaN   3.0   4.0
# b  NaN   NaN   7.0   8.0
# c  NaN   NaN  11.0  12.0
# 
#    A   B   C   D
# a  1   2   3   4
# b  5   6   7   8
# c  9  10  11  12