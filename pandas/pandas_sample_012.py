# DataFrameの連結 (concat)
# pd.concat(連結するオブジェクト, axis=0/1, join='inner'/'outer')
# axis：0 縦方向(行)、1 横方向(列) (defaultは0)
# join：'inner' 内部結合、'outer' 外部結合(defaultは'outer')

import pandas as pd

df1 =pd.DataFrame( data = [[1,2],[3,4]], index = [ 'a', 'b' ], columns = [ 'A', 'B' ] )
print(df1)
print()

df2 =pd.DataFrame( data = [[5,6],[7,8]], index = [ 'c', 'd' ], columns = [ 'B', 'C' ] )
print(df2)
print()

df3 = pd.concat( [df1, df2], join='outer' )
print(df3)
print()

df4 = pd.concat( [df1, df2], join='inner' )
print(df4)


# 実行結果
#    A  B
# a  1  2
# b  3  4
# 
#    B  C
# c  5  6
# d  7  8
# 
#      A  B    C
# a  1.0  2  NaN
# b  3.0  4  NaN
# c  NaN  5  6.0
# d  NaN  7  8.0
# 
#    B
# a  2
# b  4
# c  5
# d  7