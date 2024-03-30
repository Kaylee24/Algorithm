M, N, H = map(int, input().split())   # 상자의 크기 가로 M, 세로 N, 쌓아 올려지는 상자의 수 H
tomato = []
for h in range(H):                                                       # H개의 상자에 대하여 토마토 정보 담기
    tomato.append([list(map(int, input().split())) for _ in range(N)])   # 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 빈칸

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

day = 0
checked = [[[0] * M for _ in range(N)] for _ in range(H)]

while 1:
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
                        tomato[k + dk[z]][i + di[z]][j + dj[z]] = 1   # 토마토를 익혀준다.
                        cnt += 1
        if cnt > 0:
            day += 1

    else:                               # 작업 리스트에 토마토가 없다면
        for r in range(H):              # 상자들을 순회하며 토마토 확인
            for p in range(N):
                if 0 in tomato[r][p]:   # 안 익은 토마토가 있다면,
                    print(-1)           # 결과 -1 출력
                    exit()
        else:                           # 순회가 끝났다면,
            if day == 0:
                print(0)                # 결과 0 출력
                exit()
            print(day)
            exit()