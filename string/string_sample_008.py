# 文字列の検索 (index、rindex)
# index( 文字列, 開始位置, 終了位置 )
# 見つかった最初の位置を返す。見つからなかった場合はValueError送出
#
# rindex( 文字列, 開始位置, 終了位置 )
# 見つかった最後の位置を返す。見つからなかった場合はValueError送出

s = "aabbccddeeffaa"
print(s)
print(s.index("bb")) # "bb"がみつかった最初の位置を返す
print(s.rindex("aa")) # "aa"がみつかった最後の位置を返す
print(s.index("zz")) # "zz"は存在しないので-1
