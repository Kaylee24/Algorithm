N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maximum = 0


def dfs(x, y, temp, cnt):
    global maximum
    if cnt == 4:
        maximum = max(maximum, temp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[ny][nx]:
            continue
        visited[ny][nx] = 1
        dfs(nx, ny, temp + paper[ny][nx], cnt+1)
        visited[ny][nx] = 0


def fy(x, y):
    global maximum
    temp = paper[y][x]
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        arr.append(paper[ny][nx])
    L = len(arr)
    if L == 4:
        maximum = max(maximum, sum(arr) + paper[y][x] - min(arr))
    elif L == 3:
        maximum = max(maximum, sum(arr) + paper[y][x])
    return


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(j, i, paper[i][j], 1)
        fy(j, i)
        visited[i][j] = 0

print(maximum)
