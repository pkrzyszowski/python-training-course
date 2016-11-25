def suma(komunikat, *args): # argumenty pozycyjne; args jest tuplą; argumenty któe nazywamy są obowiązkowe
    print(komunikat)
    total = 0
    for x in args:
        total += x
    return total

def iloraz(komunikat, dzielna=0, dzielnik=1): #komunikat-arg pozycyjny i potem keyword argument-mozna podac po nazwie; wartości domyślne
    print(komunikat)
    return dzielna/dzielnik

print(iloraz('tralala', 1, 2))
print(iloraz('tralala', 3, dzielnik=4))
print(iloraz('tralala', dzielnik=5, dzielna = 10))
print(iloraz('tralala'))
print(iloraz()) #jeśli są argumenty pozycyjne i keywordy to musimy przynajmniej podac pozycyjne.  Pozycyjne musza byc przed key word
