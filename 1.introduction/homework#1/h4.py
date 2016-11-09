A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

answ = {()}

for x in A:
    tmp = set()
    for y in answ:
        tmp.add(y + (x, ))
    answ |= tmp
print(answ)