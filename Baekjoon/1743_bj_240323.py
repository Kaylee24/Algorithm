import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
waste = [list(map(int, input().split())) for _ in range(K)]   # (r, c) = (i, j)
check = [[0] * (M+1) for _ in range(N+1)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
size = []

for wi, wj in waste:                # 쓰레기 좌표 정보를 순회하며
    if check[wi][wj] == 0:          # 아직 확인하지 않은 좌표라면,
        queue = deque([[wi, wj]])   # 작업 리스트에 담아준다.
        check[wi][wj] = 1           # 확인 여부 표시를 해준다.
        s = 1                       # 쓰레기 크기 변수 설정
        while queue:
            i, j = queue.popleft()
            for k in range(4):                                 # 범위 내에서 사방을 순회하며
                p, q = i + di[k], j + dj[k]
                if 1 <= p <= N and 1 <= q <= M:
                    if [p, q] in waste and check[p][q] == 0:   # 쓰레기가 있는 좌표이면서, 확인하지 않은 좌표라면
                        queue.append([p, q])
                        check[p][q] = 1
                        s += 1
        size.append(s)

print(max(size))