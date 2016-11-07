a =  { 1: 'Poniedziałek',
       2: 'Wtorek',
       3: 'Środa',
       4: 'Czwartek',
       5: 'Piątek',
       6: 'Sobota',
       7: 'Niedziela', }

for x in list(a):
    if x % 2 != 0:
        b = dict((v, k) for (k, v) in a.items())
    else:
        del a[x]
print(b)
