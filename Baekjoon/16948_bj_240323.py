import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
chessboard = [[-1] * N for _ in range(N)]
di = [-2, -2, 0, 0, 2, 2]
dj = [-1, 1, -2, 2, -1, 1]

queue = deque([[r1, c1]])
chessboard[r1][c1] = 0
while queue:
    i, j = queue.popleft()
    if [i, j] == [r2, c2]:
        break
    for k in range(6):
        p, q = i + di[k], j + dj[k]
        if 0 <= p < N and 0 <= q < N and chessboard[p][q] == -1:
            chessboard[p][q] = chessboard[i][j] + 1
            queue.append([p, q])
print(chessboard[r2][c2])