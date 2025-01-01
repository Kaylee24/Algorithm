N, M = map(int, input().split(':'))

def gcd(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a

x = gcd(N, M)
print('%d:%d' %(N//x, M//x))