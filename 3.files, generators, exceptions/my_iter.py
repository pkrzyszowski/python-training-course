class MyIter():
    """symuluje range"""

    def __init__(self, start=0, stop=0, step=1):
        print('__init__ called')
        self.start = start
        self.stop = stop
        self.step = step
        self.curr = self.start

    def __iter__(self):
        print('__iter__ called')
        self.curr = self.start
        return self

    def __next__(self):
        print('__iter__ called')
        self.curr += self.step
        if self.curr < self.stop:
            return self.curr
        else:
            raise StopIteration

my_iter = MyIter(0, 10)
for i in my_iter:
    print(i)
print('to koniec')