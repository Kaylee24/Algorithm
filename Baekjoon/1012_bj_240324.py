import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    M, N, K = map(int, input().split())                                  # 배추밭 가로 M * 세로 N, 배추 위치 K개
    napa_cabbage = [list(map(int, input().split())) for _ in range(K)]   # 배추의 위치 X, Y (M, N)

    checked = [0]*K
    cnt = 0
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for nc_idx in range(K):
        if checked[nc_idx] == 0:
            queue = deque([napa_cabbage[nc_idx]])
            checked[nc_idx] = 1
            cnt += 1
            while queue:
                i, j = queue.popleft()
                for k in range(4):
                    p, q = i+di[k], j+dj[k]
                    if 0 <= p < M and 0 <= q < N and [p, q] in napa_cabbage:
                        idx = napa_cabbage.index([p, q])
                        if checked[idx] == 0:
                            checked[idx] = 1
                            queue.append([p, q])

    print(cnt)