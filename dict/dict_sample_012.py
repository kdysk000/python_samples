# 辞書から値を順に取り出す

test_results = { 'japanese':90, 'math':88, 'english':79, 'science':81, 'society':93 }

for subject in test_results:
    point = test_results[subject]
    print(str(subject) + ': ' + str(point))
    
