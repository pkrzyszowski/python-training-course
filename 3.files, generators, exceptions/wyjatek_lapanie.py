def divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print('Nie dzieli sie przez zero')
        print('Wyjątek: {}, typ: {}'.format(e, type(e)))

divide(1, 1)
divide(8, 2)
divide(5, 0)
