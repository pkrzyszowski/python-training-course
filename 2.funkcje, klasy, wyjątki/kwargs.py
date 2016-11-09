def kwargi(**kwargs):  #keyword arguments
    print(type(kwargs))  #typem kwargs jest słownik
    print(kwargs)

kwargi(ala=1, kot='ma')

def wszystko(a, b, ala='ma kota', *args, **kwargs):
    #print('a: {}, b: {}'.format(a, b))  ##formatowane stringow - {} zostana zastopine co jest pod a i b
    print('a: {}'.format(a))
    print('b: {}'.format(b))
    print('ala: {}'.format(ala))
    print('args: {}'.format(args))
    print('kwargs: {}'.format(kwargs))

    if 'As' in kwargs:
        print('Mamy Asa')

wszystko(1, 2)
wszystko(1, 2, 5, 6, 7, 8)
# wszystko(1, 2, 5, 6, 7, 8, ala='ma Asa') #blad
wszystko(1, 2, 5, 6, 7, 8, As='hopsa')