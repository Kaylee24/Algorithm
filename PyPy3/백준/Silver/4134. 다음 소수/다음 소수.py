def prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if x % i == 0:
            return False
    return True


import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    while True:
        if prime(N):
            print(N)
            break
        else:
            N += 1