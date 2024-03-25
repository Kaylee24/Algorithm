import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]   # O : 빈 공간, X : 벽, I : 도연, P : 사람

for i in range(N):
    if 'I' in campus[i]:
        doyeon = [i, campus[i].index('I')]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

queue = deque([doyeon])
visited = [[0] * M for _ in range(N)]
visited[doyeon[0]][doyeon[1]] = 1
cnt = 0
while queue:
    i, j = queue.popleft()
    for k in range(4):
        p, q = i+di[k], j+dj[k]
        if 0 <= p < N and 0 <= q < M and visited[p][q] == 0 and campus[p][q] != 'X':
            if campus[p][q] == 'P':
                cnt += 1
            queue.append([p, q])
            visited[p][q] = 1

if cnt == 0:
    print('TT')
else:
    print(cnt)