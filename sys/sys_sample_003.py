# 実行ファイルパス、コマンドライン引数 (sys.argv)
# argv[0]：実行ファイルパス
# argv[1]：コマンドライン引数1つ目
# arfv[2]：コマンドライン引数2つ目
#      ・
#      ・
# sys.argvはリスト型、要素の型はstr

import sys

if len(sys.argv) != 3:
    print('Invalid argument.')
    sys.exit(1)

print(type(sys.argv))
print(sys.argv)


# 実行結果
# $ python3 sys_sample_003.py 100
# Invalid argument.]
#
# $ python3 sys_sample_003.py 100 200
# <class 'list'>
# ['sys_sample_003.py', '100', '200']