def f(cnt):
    if cnt == M:
        print(*perm)
        return

    for i in range(1, N+1):
        if not visited[i]:
            perm.append(i)
            visited[i] = 1
            f(cnt+1)
            perm.pop()
            visited[i] = 0


N, M = map(int, input().split())
perm = []
visited = [0] * (N+1)

f(0)
