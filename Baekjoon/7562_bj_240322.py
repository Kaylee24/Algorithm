import sys
input = sys.stdin.readline
from collections import deque

for t in range(int(input())):
    N = int(input())                        # 체스판의 크기
    now = list(map(int, input().split()))   # 나이트가 현재 있는 칸
    to = list(map(int, input().split()))    # 나이트가 이동하려고 하는 칸

    di = [1, 1, 2, 2, -1, -1, -2, -2]
    dj = [2, -2, 1, -1, 2, -2, 1, -1]

    queue = deque([now])
    visited = [[-1] * N for _ in range(N)]
    visited[now[0]][now[1]] = 0
    while queue:
        i, j = queue.popleft()
        if i == to[0] and j == to[1]:
            break

        for k in range(8):
            p, q = i + di[k], j + dj[k]
            if 0 <= p < N and 0 <= q < N and visited[p][q] == -1:
                visited[p][q] = visited[i][j] + 1
                queue.append([p, q])

    print(visited[to[0]][to[1]])