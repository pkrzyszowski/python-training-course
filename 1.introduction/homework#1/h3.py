a =  { 1: 'Poniedziałek',
       2: 'Wtorek',
       3: 'Środa',
       4: 'Czwartek',
       5: 'Piątek',
       6: 'Sobota',
       7: 'Niedziela', }

keys = list(a.keys())
for k in keys:
    if k % 2 == 1:
        a[a[k]] = k
    del a[k]
print(a)