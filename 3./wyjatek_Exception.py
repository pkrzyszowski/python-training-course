def divide(a, b):
    try:
        print(*a/b)  ### oznacza, ze to zostanie rozpakowane do listy argumentów
    except Exception as e:
        print('Nie dzieli sie przez zero')
        print('wyjatek: {}'.format(e))
        raise

# divide(1, 0)
# divide([1, 2], 4)
# divide(8, 2)

def my_divide(a, b):
    try:
        divide([1, a], b)
    except Exception:
        print('akuku')

my_divide(8, 2)