# 余分な文字の除去 (strip、rstrip)
# strip( 除去する文字 )
# rstrip( 除去する文字 )
# strip()は文字列の先頭と末尾にある余分な文字を除去する
# rstrip()は文字列の末尾にある余分な文字を除去する

s = "  Hello World \n"
print(s)
print(s.strip())
print(s.rstrip()) # 先頭の空白は除去されない
