def odlicz(n):
    if n <= 0:
        print('Odpalamy!')
    else:
        print(n)
        odlicz(n - 1)

odlicz(3)

def drukuj_n(s, n):
    if n <= 0:
        return
    print(s)
    drukuj_n(s, n - 1)

drukuj_n('string', -1)