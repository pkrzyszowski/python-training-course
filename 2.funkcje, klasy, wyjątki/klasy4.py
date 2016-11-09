class Point():  # przy tworzeniu klasu najpierw __new__() potem __init__()
    def __init__(self, x, y):
        print('tworzę nową instancję punktu w: ({}, {})'.format(x, y))
        self.x = x
        self.y = y

    def where_am_i(self):
        print('x: {}, y: {}'.format(self.x, self.y))

    def hello(self):
        print('Hello tu: {}, id: {}'.format(type(self), id(self)))


a = Point(1, 2)
print(type(a))
print(id(a))
a.where_am_i()
print(a.x)
print(a.y)

b = Point(3,4)
print(type(b))
print(id(b))
b.where_am_i()
print(b.x)
print(b.y)

c = Point(5, 6)
c.where_am_i()