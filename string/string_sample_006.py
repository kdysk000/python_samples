# 文字列の検索 (count)
# count( 文字列, 開始位置, 終了位置 )
# 引数で指定した文字列が何個含まれているかを返す

s = "aabbccddeeffaa"
print(s)
print(s.count("aa")) # 先頭から"aa"が何個含まれるかを検索
print(s.count("aa", 1)) # 2文字目から"aa"が何個含まれるかを検索
