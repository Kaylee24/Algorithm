def f(k, j, result):
    if k == M:
        print(*result)
    else:
        for i in range(j, N):
            result.append(nums[i])
            f(k+1, i+1, result)
            result.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []
f(0, 0, result)