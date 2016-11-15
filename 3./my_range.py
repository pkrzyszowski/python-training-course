def my_range(start=0, stop=0, step=1):
    '''udaje range'''
    curr = start
    while curr < stop:
        yield curr
        curr += step

a = my_range(1, 2)
print(a)
print(next(a))
# print(next(a))

for i in my_range(0, 11, 2):
    print(i)