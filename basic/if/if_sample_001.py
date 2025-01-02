# if 条件式1 :
#     処理A
# elif 条件式2 :
#     処理B
# else :
#     処理C

from random import randint

num = randint(0, 100)

if num >= 80 :
    ret = "A"
elif num >= 60 :
    ret = "B"
elif num >= 40 :
    ret = "C"
else :
    ret = "D"

print(ret)