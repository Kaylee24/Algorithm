'19:28 / 목표 20:20 (1/3) / ~19:42'

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
treasure = [list(input()) for _ in range(N)]   # 'L' : 육지, 'W' : 바다
maximum = 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if treasure[i][j] == 'L':   # 방문하지 않은 육지라면
            queue = deque([[i, j]])
            visited = [[-1] * M for _ in range(N)]
            visited[i][j] = 0
            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    p, q = y + di[k], x + dj[k]
                    if 0 <= p < N and 0 <= q < M and treasure[p][q] == 'L' and visited[p][q] == -1:
                        visited[p][q] = visited[y][x] + 1
                        queue.append([p, q])
                        if maximum < visited[p][q]:
                            maximum = visited[p][q]

print(maximum)