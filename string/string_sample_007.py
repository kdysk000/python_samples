# 文字列の検索 (find、rfind)
# find( 文字列, 開始位置, 終了位置 )
# 見つかった最初の位置を返す。見つからなかった場合は-1を返す
#
# rfind( 文字列, 開始位置, 終了位置 )
# 見つかった最後の位置を返す。見つからなかった場合は-1を返す

s = "aabbccddeeffaa"
print(s)
print(s.find("bb")) # "bb"がみつかった最初の位置を返す
print(s.rfind("aa")) # "aa"がみつかった最後の位置を返す
print(s.find("zz")) # "zz"は存在しないので-1
