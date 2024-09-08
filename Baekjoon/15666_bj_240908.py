def f(k, j):
    p = 0

    if k == M:
        print(*perm)
    else:
        for i in range(j, N):
            if nums[i] != p:
                p = nums[i]
                perm.append(p)
                f(k+1, i)
                perm.pop()


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

perm = []
f(0, 0)