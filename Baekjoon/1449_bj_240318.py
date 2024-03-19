import sys

N, L = map(int, sys.stdin.readline().split())
where = list(map(int, sys.stdin.readline().split()))
where.sort()
taped = [0] * (where[-1] + L)
cnt = 0

for i in range(N):
    if taped[where[i]] == 0:
        taped[where[i] : L] = [1] * L
        cnt += 1

print(cnt)