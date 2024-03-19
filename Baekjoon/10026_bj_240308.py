N = int(input())   # 그림의 크기 N*N
color = [['-'] + list(input()) + ['-'] for _ in range(N)]   # 그림 : 빨강 R, 초록 G, 파랑 B
color.insert(0, ['-'] * (N + 2))
color.append(['-'] * (N + 2))
special_color = [['-'] * (N+2) for _ in range(N+2)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if color[i][j] in ['R', 'G']:
            special_color[i][j] = 'RG'
        else:
            special_color[i][j] = 'B'

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

ordinary_visited = [[0] * (N+2) for _ in range(N+2)]
special_visited = [[0] * (N+2) for _ in range(N+2)]
q = []
ordinary_cnt = 0        # 구역 개수
special_cnt = 0        # 구역 개수
ordinary_visited_cnt = 0
special_visited_cnt = 0
t = [1, 1]

while ordinary_visited_cnt < N**2:
    stop = False
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if ordinary_visited[i][j] == 0:
                q.append([i, j])
                ordinary_visited[i][j] = 1  # 방문 표시
                ordinary_visited_cnt += 1
                ordinary_cnt += 1
                stop = True
                break
        if stop:
            break

    while q:
        t = q.pop(0)

        for k in range(4):        # 델타 탐색으로 본인과 같고, 방문하지 않은 칸이면 작업 리스트 q 에 append 해준다.
            if color[t[0]][t[1]] == color[t[0] + di[k]][t[1] + dj[k]] and ordinary_visited[t[0] + di[k]][t[1] + dj[k]] == 0:
                q.append([t[0] + di[k], t[1] + dj[k]])
                ordinary_visited[t[0] + di[k]][t[1] + dj[k]] = 1  # 방문 표시
                ordinary_visited_cnt += 1

while special_visited_cnt < N**2:
    stop = False
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if special_visited[i][j] == 0:
                q.append([i, j])
                special_visited[i][j] = 1  # 방문 표시
                special_visited_cnt += 1
                special_cnt += 1
                stop = True
                break
        if stop:
            break

    while q:
        t = q.pop(0)

        for k in range(4):        # 델타 탐색으로 본인과 같고, 방문하지 않은 칸이면 작업 리스트 q 에 append 해준다.
            if special_color[t[0]][t[1]] == special_color[t[0] + di[k]][t[1] + dj[k]] and special_visited[t[0] + di[k]][t[1] + dj[k]] == 0:
                q.append([t[0] + di[k], t[1] + dj[k]])
                special_visited[t[0] + di[k]][t[1] + dj[k]] = 1  # 방문 표시
                special_visited_cnt += 1

print(ordinary_cnt, special_cnt)