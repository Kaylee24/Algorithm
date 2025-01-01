import math

N, M = map(int, input().split(':'))

gcd = math.gcd(N, M)

N //= gcd
M //= gcd

print(f"{N}:{M}")