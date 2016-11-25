class A():
    def hello(self):
        print('jestem A')

class B():
    def hello(self):
        print('jestem B')

class C(A, B):
    pass

c = C()
c.hello()

# MRO - method resolution order = rozwiazuje dla interpretera konflikty których nie zauwazyl uzytkownik np. przy dziedziczeniu wielokrotnym

class D(B, A):
    pass

d = D()
d.hello()