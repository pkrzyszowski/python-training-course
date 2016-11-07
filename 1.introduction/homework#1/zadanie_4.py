from itertools import combinations

A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

subsets = set(y for y in range(len(A)+1) for y in combinations(A,y))
subsets_sorted = sorted(subsets, key = len)

print(subsets)
print(subsets_sorted)