def f(k):
    if k == N:
        result = 0
        for i in range(N-1):
            result += abs(perm[i] - perm[i+1])
        results.append(result)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                perm.append(A[i])
                f(k+1)
                visited[i] = 0
                perm.pop()


import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

visited = [0] * N
perm = []
results = []
f(0)
print(max(results))