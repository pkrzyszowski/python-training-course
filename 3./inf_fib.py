def inf_fib():
    '''generuje kolejne liczby cagu Fibbonaciego'''
    a, b = 0, 1
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a, b = b, c

for i in inf_fib():
    print(i)