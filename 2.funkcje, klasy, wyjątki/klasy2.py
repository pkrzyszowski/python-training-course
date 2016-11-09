class  NazwaKlasy():
    def hello(self):
        print('Hello tu: {}, id: {}'.format(type(self), id(self)))

a = NazwaKlasy()
print(type(a))
print(id(a))
a.hello()

b = NazwaKlasy()
print(type(b))
print(id(b))
b.hello()

print(type(NazwaKlasy))
print(id(NazwaKlasy))


c = [1, 2, 3]
print(c.__len__())
print(len(c))

print(c.__str__())