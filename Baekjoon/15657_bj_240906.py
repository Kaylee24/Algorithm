def f(k, last_idx):
    if k == M:
        print(*result)
    else:
        for i in range(last_idx, N):
            result.append(nums[i])
            f(k+1, i)
            result.pop()


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = []
f(0, 0)
