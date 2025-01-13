N, M = map(int, input().split())


def two_f(x):
    two = 0
    while x > 0:
        x //= 2
        two += x
    return two


def five_f(x):
    five = 0
    while x > 0:
        x //= 5
        five += x
    return five


print(min(two_f(N)-two_f(N-M)-two_f(M), five_f(N)-five_f(N-M)-five_f(M)))