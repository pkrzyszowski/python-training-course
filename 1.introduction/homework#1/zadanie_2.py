a = []

for y in range(101):
    b = [x for x in range(101)]
    a.append(b)
    b.append(sum(range(b[y] + 1)))

print(a)
