# CSV読み込み (read_csv)(index_col、usecols)
# pd.read_csv( CSVファイルパス, header=ヘッダー行番号, index_col=index列番号, usecols=列番号 )
# header：指定なしの場合は0行目
# index_col：指定なしの場合はindex列は認識されない
# usecols：読み込む列の指定

import pandas as pd

df =pd.read_csv('./data/data.csv')
print(df)
print()

# lambda (特定の列を除外して読み込む)
df =pd.read_csv('./data/data.csv', index_col=0, usecols=lambda x: x != 'C')  # C列以外を読み込む
print(df)


# 実行結果
#   Unnamed: 0   A   B   C   D
# 0          a   1   2   3   4
# 1          b   5   6   7   8
# 2          c   9  10  11  12
# 3          d  13  14  15  16
# 
#     A   B   D
# a   1   2   4
# b   5   6   8
# c   9  10  12
# d  13  14  16