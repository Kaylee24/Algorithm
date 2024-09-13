def f(k):
    last = 0

    if k == M:
        print(*result)
    else:
        for i in range(N):
            if visited[i] == 0 and nums[i] != last:
                visited[i], last = 1, nums[i]
                result.append(nums[i])
                f(k+1)
                visited[i] = 0
                result.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * N
result = []
f(0)