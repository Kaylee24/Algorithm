import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
max_P = P[:]

for i in range(1, N+1):
    for j in range(i//2 + 1):
        temp = max_P[i-j] + max_P[j]
        if temp > max_P[i]:
            max_P[i] = temp

print(max_P[N])