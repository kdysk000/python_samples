# 文字列の置換 (replace)
# replace( 検索文字列, 置換文字列, 個数 )
# 個数の指定なしの場合は全て置換される

s = "aabbccddeeffaa"
print(s)
print(s.replace("aa", "zz"))


# 実行結果
# aabbccddeeffaa
# zzbbccddeeffzz