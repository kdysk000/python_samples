# ソート
#
# sort_index(ascending=True/False, inplace=True/False)
# ascending：True 昇順、False 降順 (defaultはTrue)
# inplace：True ソート結果で置き換える、False ソート結果で置き換えない (defaultはFalse)
#
# sort_values(by=列名, ascending=True/False, inplace=True/False)
# ascending：True 昇順、False 降順 (defaultはTrue)
# inplace：True ソート結果で置き換える、False ソート結果で置き換えない (defaultはFalse)

import pandas as pd

df =pd.DataFrame( data = [[1,2,3],[4,5,6],[7,8,9]], index = [ 'a', 'b', 'c' ], columns = [ 'X', 'Y', 'Z' ] )
print(df)
print()

# indexでソート
df.sort_index(ascending=False, inplace=True)
print(df)
print()

# 指定列でソート
df.sort_values(by='X', ascending=True, inplace=True)
print(df)

# 実行結果
#    X  Y  Z
# a  1  2  3
# b  4  5  6
# c  7  8  9
# 
#    X  Y  Z
# c  7  8  9
# b  4  5  6
# a  1  2  3
# 
#    X  Y  Z
# a  1  2  3
# b  4  5  6
# c  7  8  9