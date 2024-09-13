def f(k, result):
    if k == M:
        print(*result)
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                result.append(nums[i])
                f(k+1, result)
                visited[i] = 0
                result.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [0] * N
result = []
f(0, result)