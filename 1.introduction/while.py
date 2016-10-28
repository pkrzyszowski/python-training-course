limit=100
for n in range(3, limit):
    q = 2
    while q < n:
        if n % q == 0:
            break
        q += 1
    else:
        print(n, 'jst liczbą pierwszą')
