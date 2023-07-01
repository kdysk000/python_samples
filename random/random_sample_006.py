# リストからランダムに要素を抽出しリストで返す (random.sample)
# random.sample(リスト, 抽出する要素数)

import random

numbers = [1, 2, 3, 4, 5]
sample = random.sample(numbers, 3)
print(sample)


# 実行結果
# [4, 5, 3]