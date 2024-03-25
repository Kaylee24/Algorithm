import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]   # 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 빈칸
riped = [[-1] * M for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
cnt, day = 0, 0

queue = deque([])
for i in range(N):                 # 칸들을 순회하며
    for j in range(M):
        if tomato[i][j] == 1:      # 익은 토마토라면
            queue.append([i, j])   # 작업 리스트에 추가
            riped[i][j] = 0
            cnt += 1               # '익은 토마토'와 빈칸 수 세기
        elif tomato[i][j] == -1:   # 익은 토마토와 '빈칸' 수 세기
            cnt += 1
if cnt == N * M:   # 모든 토마토가 익어있는 상태라면 0을 출력한다.
    print(0)
else:              # 안 익은 토마토가 있다면,
    while queue:
        y, x = queue.popleft()                                    # 처음부터 익어있던 토마토들을 순회하며
        for k in range(4):                                        # 사방의 토마토들을 확인한다.
            p, q = y + di[k], x + dj[k]
            if 0 <= p < N and 0 <= q < M and riped[p][q] == -1:   # 상자 내의 좌표이고, 아직 확인한 적 없는 칸이고,
                if tomato[p][q] == 0:                             # 안 익은 토마토라면,
                    tomato[p][q] = 1                              # 토마토를 익히고
                    riped[p][q] = riped[y][x] + 1                 # 토마토가 익는데 걸린 날짜 정보를 업데이트 해준다.
                    queue.append([p, q])
                    cnt += 1                                      # 이제 토마토가 익었으므로 cnt 도 세준다.
                    if day < riped[p][q]:   # 토마토가 익는데 걸린 최종 날짜를 업데이트 해준다.
                        day = riped[p][q]

    if cnt == N * M:   # 최종적으로 모든 토마토가 익었다면, 익는데 걸린 날짜를 출력한다.
        print(day)
    else:              # 못 익는 토마토가 있다면, -1 을 출력한다.
        print(-1)