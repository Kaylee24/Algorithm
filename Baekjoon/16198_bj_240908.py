def f(k, eng):
    if k == N-2:
        energy.append(eng)
    else:
        for i in range(1, N-1-k):
            temp = marbles[i-1] * marbles[i+1]
            m = marbles.pop(i)
            f(k+1, eng+temp)
            marbles.insert(i, m)


import sys
input = sys.stdin.readline

N = int(input())
marbles = list(map(int, input().split()))
energy = []

f(0, 0)

print(max(energy))