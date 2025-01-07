N, M, K = map(int, input().split())
board = []

for i in range(N):
    board += list(map(int, input().split()))

answer = []
visited = [0 for i in range(N*M)]
maximum = float('-inf')


def f(cnt, sums, now):
    global maximum

    if cnt == K:
        if sums > maximum:
            maximum = sums
        return

    for i in range(now, N*M):
        if (i % M > 0 and visited[i-1]) or (i >= M and visited[i-M]):
            continue
        else:
            visited[i] = 1
            f(cnt+1, sums+board[i], i+1)
            visited[i] = 0


f(0, 0, 0)
print(maximum)
