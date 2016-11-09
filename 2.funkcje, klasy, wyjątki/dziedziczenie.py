class A():
    def hello(self):
        print('jestem instancją A')

class B(A):   #w python3 kazda klasa dziedziczy po object (roznica z python2)
    def hi(self):
        print('jestem instancją B')

a = A()
b = B()

print(type(A))
print(type(B))

a.hello()
b.hello()
b.hi()
## a.hi() #dzedziczenie tylko w jedna strone

class C(B):
    pass

c = C()
c.hello()
c.hi()