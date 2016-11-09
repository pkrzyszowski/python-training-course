def pow(a, b):
    print('podniosę {} do potęgi {}'.format(a, b))
    return a**b

print(pow(1, 2))

c = pow

print(c(3, 4))

print(type(pow))
print(id(pow))
print(type(c))
print(id(c))