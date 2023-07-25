# 文字列の置換(replace)
#
# replace( 置換対象の文字列, 置換文字列, 置換する個数 )

s1 = 'My name is Taro.'
ss1 = s1.replace('Taro', 'Jiro')
print(ss1)

s2 = 'Hello Hello'
ss2 = s2.replace('Hello', 'Bye')  # 第3引数を指定しなければすべて置換される
print(ss2)

s3 = 'World World'
ss3 = s3.replace('World', 'Hello', 1)  # 第4引数で置換する個数を指定
print(ss3)

# 実行結果
# My name is Jiro.
# Bye Bye
# Hello World