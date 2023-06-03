# CSV読み込み
# pd.read_csv( CSVファイルパス, header=ヘッダー行番号, index_col=index列番号, usecols=列番号 )
# header：指定なしの場合は0行目
# index_col：指定なしの場合はindex列は認識されない
# usecols：読み込む列の指定

import pandas as pd

df =pd.read_csv('./data/data.csv')
print(df)
print()

df =pd.read_csv('./data/data.csv', index_col=0)
print(df)