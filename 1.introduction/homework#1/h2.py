zero_sto = list(range(101))

total = 0

answ = [None] * 100
for i in range(100):
    a = zero_sto[:] #skopiowanie listy zero_sto
    total += i
    a.append(total)
    answ[i]

print(answ)