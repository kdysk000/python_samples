# リストの要素をランダムにシャッフルする (random.shuffle)
# random.shuffle(リスト)

import random

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

random.shuffle(numbers)
print(numbers)


# 実行結果
# [1, 2, 3, 4, 5, 6]
# [6, 5, 2, 1, 4, 3]