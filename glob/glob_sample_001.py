# 特定のパターンにマッチするファイルを取得する (glob.glob)

import glob

# dataフォルダのTXTファイルを取得 (サブフォルダ内のファイルは対象外)
file = glob.glob('data/*.txt')
print(file)

# dataフォルダにあるサブフォルダ内のTXTファイル全てを取得
file = glob.glob('data/**/*.txt')
print(file)

# dataフォルダ以下のTXTファイル全てを取得
file = glob.glob('data/**/*.txt', recursive=True)
print(file)

# dataフォルダ以下のJSONファイル全てを取得
file = glob.glob('data/**/*.json', recursive=True)
print(file)


# 実行結果
# ['data/test2.txt', 'data/test1.txt']
# ['data/test1/c.txt', 'data/test1/a.txt', 'data/test2/c.txt']
# ['data/test2.txt', 'data/test1.txt', 'data/test1/c.txt', 'data/test1/a.txt', 'data/test2/c.txt']
# ['data/test1.json', 'data/test1/b.json', 'data/test2/d.json']