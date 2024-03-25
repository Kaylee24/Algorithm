from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

'bfs'
queue = deque([[0, 0]])
visited = [[-1] * M  for _ in range(N)]
visited[0][0] = 1
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
while queue:
    i, j = queue.popleft()
    if i == N-1 and j == M-1:
        break

    for k in range(4):
        p, q = i + di[k], j + dj[k]
        if 0 <= p < N and 0 <= q < M and visited[p][q] == -1:
            if maze[p][q] == '1':
                visited[p][q] = visited[i][j] + 1
                queue.append([p, q])
            elif maze[p][q] == '0':
                visited[p][q] = 0

print(visited[N-1][M-1])