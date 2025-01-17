from itertools import *

vowels = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
arr = list(input().split())
pws = []

for com in combinations(sorted(arr), L):
    v = sum(x in vowels for x in com)
    if v >= 1 and L - v >= 2:
        pws.append(com)

for pw in pws:
    print(''.join(pw))