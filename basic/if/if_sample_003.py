# 論理演算 (or)
# if 条件式1 and 条件式2 :
#     処理A
# else :
#     処理C

from random import randint

size = randint(5, 20)
weight = randint(20, 40)

if size >= 10 or weight >= 25 :
    ret = "A"
else :
    ret = "B"

print("size:", size)
print("weight:", weight)
print(ret)