import math

A, B = map(int, input().split())
C, D = map(int, input().split())

L = math.lcm(B, D)
E = A*(L//B) + C*(L//D)

X = math.gcd(E, L)

print(int(E/X), int(L/X))