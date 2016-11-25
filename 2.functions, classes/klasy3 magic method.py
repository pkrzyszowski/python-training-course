class  NazwaKlasy():  #przy tworzeniu klasu najpierw __new__() potem __init__()
    def __init__(self):
        print('tworzę nową instancję')

    def hello(self):
        print('Hello tu: {}, id: {}'.format(type(self), id(self)))

a = NazwaKlasy()
# print(type(a))
# print(id(a))
a.hello()

b = NazwaKlasy()
# print(type(b))
# print(id(b))
# b.hello()
#
# print(type(NazwaKlasy))
# print(id(NazwaKlasy))
