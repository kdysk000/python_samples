# 辞書の複製 (copy)
# 複製した辞書を更新しても元の辞書には影響しない

test_results = { 'japanese':90, 'math':88, 'english':79, 'science':81, 'society':93 }
test_results_copy = test_results.copy()
test_results_copy['japanese'] = 91

print(test_results)
print(test_results_copy)
