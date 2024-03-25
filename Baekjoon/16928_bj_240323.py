'19:44 / 목표 20:20 (2/3) / ~20:25'

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())   # 사다리의 수 N, 뱀의 수 M (1 <= N, M <= 15)
ladder = [list(map(int, input().split())) for _ in range(N)]   # [x, y] : x -> y 이동
snake = [list(map(int, input().split())) for _ in range(M)]    # [u, v] : x -> y 이동
ladder.sort(key=lambda x: x[0])
snake.sort(key=lambda x: x[0])
ladder_start, snake_start = [], []
for L in ladder:
    ladder_start.append(L[0])
for S in snake:
    snake_start.append(S[0])
visited = [[-1] * 10 for _ in range(10)]

# X 번째 칸의 좌표 = [(X-1)//10, (X-1)%10]
queue = deque([[0, 0]])
visited[0][0] = 0

while queue:
    y, x = queue.popleft()
    X = (y*10 + x) + 1
    if X == 100:
        break

    # 사다리가 있는 칸이라면
    if X in ladder_start:
        idx = ladder_start.index(X)
        to = ladder[idx][1]
        to_p, to_q = (to - 1) // 10, (to - 1) % 10
        visited[to_p][to_q] = visited[y][x]
        queue.appendleft([to_p, to_q])

    # 뱀이 있는 칸이라면
    elif X in snake_start:
        idx = snake_start.index(X)
        to = snake[idx][1]
        to_p, to_q = (to - 1) // 10, (to - 1) % 10
        if visited[to_p][to_q] == -1:
            visited[to_p][to_q] = visited[y][x]
            queue.appendleft([to_p, to_q])

    # 사다리도, 뱀도 없는 칸이라면
    else:
        for k in range(1, 7):
            p, q = (X-1+k)//10, (X-1+k)%10
            if 1 <= X+k <= 100 and visited[p][q] == -1:
                visited[p][q] = visited[y][x] + 1
                queue.append([p, q])

print(visited[9][9])

