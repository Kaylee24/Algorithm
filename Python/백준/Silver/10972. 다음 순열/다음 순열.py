N = int(input())
perm = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if perm[i-1] < perm[i]:   # 오름차순인 구간이라면,
        for j in range(N-1, 0, -1):
            if perm[i-1] < perm[j]:
                perm[i-1], perm[j] = perm[j], perm[i-1]
                perm = perm[:i] + sorted(perm[i:])
                exit(print(*perm))

print(-1)