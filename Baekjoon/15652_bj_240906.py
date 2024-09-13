def f(k, result):
    if k == M:
        print(*result)
    else:
        j = 1
        if result:
            j = result[-1]

        for i in range(j-1, N):
            result.append(nums[i])
            f(k+1, result)
            result.pop()


N, M = map(int, input().split())
nums = list(range(1, N+1))

result = []
f(0, result)