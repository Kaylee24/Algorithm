def f(k, result):
    if k == M:
        print(*result)
    else:
        for i in range(N):
            result.append(nums[i])
            f(k+1, result)
            result.pop()


N, M = map(int, input().split())
nums = list(range(1, N+1))

result = []
f(0, result)