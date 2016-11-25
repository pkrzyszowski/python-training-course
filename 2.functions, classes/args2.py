def suma(*args): # args jest tuplą
    total = 0
    for x in args:
        total += x
    return total
print(suma(1, 2, 3, 4, 5))
print(suma(1))
print(suma())

# sum()