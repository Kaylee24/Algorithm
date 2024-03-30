import sys
sys.setrecursionlimit(1000000)

def ripe(day):
    q = []
    cnt = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[k][i][j] == 1 and checked[k][i][j] == 0:   # 익은 토마토이면서, 아직 확인하지 않은 토마토라면,
                    q.append([k, i, j])                              # 작업 리스트 q 에 담기.
                    checked[k][i][j] = 1                             # 그리고 확인한 토마토라고 표시

    if len(q) > 0:   # 작업 리스트에 토마토가 있다면
        while q:
            k, i, j = q.pop()
            for z in range(6):  # 6방향을 순회하며
                if 0 <= k + dk[z] < H and 0 <= i + di[z] < N and 0 <= j + dj[z] < M:
                    if tomato[k + dk[z]][i + di[z]][j + dj[z]] == 0:  # 익지 않은 토마토라면,
                        tomato[k + dk[z]][i + di[z]][j + dj[z]] = 1  # 토마토를 익혀준다.
                        cnt += 1
        ripe(day+1)

    else:                               # 작업 리스트에 토마토가 없다면
        for r in range(H):              # 상자들을 순회하며 토마토 확인
            for p in range(N):
                if 0 in tomato[r][p]:   # 안 익은 토마토가 있다면,
                    return print(-1)    # 결과 -1 출력
        else:                           # 순회가 끝났다면,
            if day == 0:
                return print(0)             # 결과 0 출력
            if day == 1 and cnt == 0:
                return print(0)
            if cnt == 0:
                return print(day - 1)
            return print(day)



M, N, H = map(int, input().split())   # 상자의 크기 가로 M, 세로 N, 쌓아 올려지는 상자의 수 H
tomato = []
for h in range(H):                                                       # H개의 상자에 대하여 토마토 정보 담기
    tomato.append([list(map(int, input().split())) for _ in range(N)])   # 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 빈칸

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

checked = [[[0] * M for _ in range(N)] for _ in range(H)]

ripe(0)

'''
순회하면서 익은 토마토만 q 에 담는다.
이때 q 에 담은 친구들은 작업완료 했음을 따로 표시해준다.(visited)
t 를 기준으로 위, 아래, 상하좌우 총 6방향을 살피고,
안익은 토마토 (0) 이라면 1로 바꿔준다.
q 가 비면 하루가 끝난것.

또 순회한다.
작업을 완료하지 않았고, 익은 토마토만 q 에 담는다.
반복한다.

q 에 담을 것이 없다면,
결과를 살핀다.
0 이 없다면 다 익은 것이고, 0 이 있다면 다 익지 않은 것이다.
'''