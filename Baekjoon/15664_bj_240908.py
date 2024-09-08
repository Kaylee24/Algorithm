import sys
input = sys.stdin.readline

def f(k, j):
    p = 0

    if k == M:
        print(*perm)
    else:
        for i in range(j, N):
            if nums[i] != p:
                perm.append(nums[i])
                p = nums[i]
                f(k+1, i+1)
                perm.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

perm = []
f(0, 0)