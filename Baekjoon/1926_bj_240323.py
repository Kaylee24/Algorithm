import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
drawing = [list(map(int, input().split())) for _ in range(N)]   # 0 : 색칠이 안된 부분, 1 : 색칠이 된 부분
check = [[0] * M for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
cnt = 0
size = [0]

for i in range(N):
    for j in range(M):
        if check[i][j] == 0:
            check[i][j] = 1
            if drawing[i][j] == 1:
                queue = deque([[i, j]])
                cnt += 1
                s = 1
                while queue:
                    y, x = queue.popleft()
                    for k in range(4):
                        p, q = y + di[k], x + dj[k]
                        if 0 <= p < N and 0 <= q < M and drawing[p][q] == 1 and check[p][q] == 0:
                            queue.append([p, q])
                            check[p][q] = 1
                            s += 1
                size.append(s)

print(cnt)
print(max(size))