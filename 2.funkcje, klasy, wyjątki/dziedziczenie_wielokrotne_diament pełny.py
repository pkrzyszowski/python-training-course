class BaseAB():
    def hello_ab(self):
        print('BaseAB')

class A(BaseAB):
    def hello(self):
        print('jestem A')

class B(BaseAB):
    def hello(self):
        print('jestem B')

class C(A, B):
    pass


c = C()
c.hello_ab()