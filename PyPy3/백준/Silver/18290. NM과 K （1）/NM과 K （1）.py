def f(cnt, sums):
    global maximum

    if cnt == K:
        if maximum < sums:
            maximum = sums
        return

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:   # 아직 방문하지 않은 칸이라면, 인접한 칸 중 선택한 칸이 없는지 확인
                if (i >= 1 and visited[i-1][j]) or (j >= 1 and visited[i][j-1]) or (i < N-1 and visited[i+1][j]) or (j < M-1 and visited[i][j+1]):
                    continue
                else:
                    visited[i][j] = 1
                    f(cnt+1, sums+board[i][j])
                    visited[i][j] = 0


N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]

maximum = float('-inf')

f(0, 0)
print(maximum)
