# 辞書内包表記
# { キー:値 for キー in イテラブル }

from random import randint

subjects = { 'japanese', 'math', 'english', 'science', 'society' }
test_results = { subject: randint(1,100) for subject in subjects }
print(test_results)


# 実行結果
# {'society': 22, 'science': 65, 'english': 18, 'japanese': 19, 'math': 81}