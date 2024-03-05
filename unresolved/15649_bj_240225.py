def f(k, result):
    if k == M:
        print(*result)

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                result.append(number[i])
                f(k + 1, result)
                visited[i] = 0
                result.pop()

N, M = map(int, input().split())
number = list(range(1, N + 1))

visited = [0] * N
result = []
f(0, result)