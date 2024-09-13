def f(k, result):
    if k == M:
        print(*result)
    else:
        j = 0
        if result:
            j = result[-1]

        for i in range(j, N):
            if visited[i] == 0:
                visited[i] = 1
                result.append(nums[i])
                f(k+1, result)
                visited[i] = 0
                result.pop()


N, M = map(int, input().split())
nums = list(range(1, N+1))

visited = [0] * N
result = []
f(0, result)
