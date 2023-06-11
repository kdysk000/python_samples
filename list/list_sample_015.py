#複数リストの要素を順に取り出す (zip)

name1 = [ 'suzuki ', 'tanaka ', 'yamamoto ', 'sato ' ]
name2 = [ 'ichiro', 'jiro', 'saburo', 'siro' ]
fullname = []

for n1, n2 in zip(name1, name2):
    fullname.append(n1+n2)
print(fullname)