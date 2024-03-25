'''
오전 -> 안됨
동일 유형 bfs 몇문제 더 풀고 밤에 재도전 -> 안됨
'질문 게시판'의 힌트글 보고 해결
'''
from collections import deque

for T in range(int(input())):   # 테스트 케이스 수 T
    N = int(input())            # 편의점의 개수 N
    node = [list(map(lambda x: int(x)+32768, input().split())) for _ in range(N+2)]   # [x, y], 두 좌표 사이의 거리 = abs(x1-x2) + abs(y1-y2)
    home, *conv = node
    rock = conv[-1]
    adjl = [[] for _ in range(N+2)]
    # 모든 지점 간의 거리가 20 * 50 이하인지 확인한다.
    # 만약 초과이면 sad, 이하이면 happy

    for i in range(N+2):
        for j in range(N+2):
            if i != j:         # 서로 다른 지점들에 대해 완전 탐색 시행
                dist = abs(node[i][0]-node[j][0]) + abs(node[i][1]-node[j][1])
                if 0 <= dist <= 50*20:
                    adjl[i].append(j)
                    adjl[j].append(i)

    if adjl.count([]) == N+2:
        print('sad')
    else:
        how_are_you = 'sober'
        queue = deque([0])
        visited = [0] * (N+2)
        visited[0] = 1
        while queue:
            now = queue.popleft()
            if now == N+1:
                how_are_you = 'drunken'
                print('happy')
                break
            for to in adjl[now]:
                if visited[to] == 0:
                    visited[to] = 1
                    queue.append(to)
        if how_are_you == 'sober':
            print('sad')





'''
# 두번째 풀이

from collections import deque

for T in range(int(input())):   # 테스트 케이스 수 T
    N = int(input())            # 편의점의 개수 N
    node = [list(map(lambda x: int(x)+32768, input().split())) for _ in range(N+2)]   # [x, y], 두 좌표 사이의 거리 = abs(x1-x2) + abs(y1-y2)
    home, *conv = node
    rock = conv[-1]
    node.sort(key=lambda x: sum(x))
    # 모든 지점 간의 거리가 20 * 50 이하인지 확인한다.
    # 만약 초과이면 sad, 이하이면 happy

    how_are_you = 'drunken'
    for i in range(1, N+2):
        dist = abs(node[i][0]-node[i-1][0]) + abs(node[i][1]-node[i-1][1])
        if dist > 50*20:
            how_are_you = 'sober'   # 거리 조건을 만족시키지 못하는 지점이 있다면 'sad' 결과 출력 및 해당 테스트케이스 코드 종료
            print('sad')
            break

    if how_are_you == 'drunken':    # 거리 조건을 모두 만족시켰다면 bfs 실행
        how_are_you = 'sober'
        queue = deque([home])
        visited = []
        visited.append(home)
        while queue:
            i, j = queue.popleft()
            if [i, j] == rock:
                how_are_you = 'drunken'
                print('happy')
                break
            for p, q in conv:
                if abs(i-p) + abs(j-q) <= 50*20 and [p, q] not in visited:
                    visited.append([p, q])
                    queue.append([p, q])
        if how_are_you == 'sober':
            print('sad')
'''

'''
# 첫번째 풀이

from collections import deque

for T in range(int(input())):   # 테스트 케이스 수 T
    N = int(input())            # 편의점의 개수 N
    Home, *Conv, Rock = [list(map(int, input().split())) for _ in range(N+2)]   # [x, y], 두 좌표 사이의 거리 = abs(x1-x2) + abs(y1-y2)

    queue = deque([Home])                        # 작업 리스트
    beer = [[0] * 65536 for _ in range(65536)]   # 지도, 남은 맥주 병 표시
    beer[Home[0]+32768][Home[1]+32768] = 19      # 출발지점에서 맥주 마시고 출발하므로 출발 지점은 맥주 19병
    di = [1, -1, 1, -1]
    dj = [1, 1, -1, -1]
    while deque:
        i, j = queue.popleft()
        if [i, j] == Rock:                       # 작업 대상 좌표가 도착지점이라면 반복문 종료
            break
        if beer[i][j] == 0:                      # 작업 대상 좌표에 남은 맥주가 없다면 다음 작업 대상으로 넘어가기
            pass
        else:                                    # 작업 가능한 좌표라면
            for d in range(4):                   # 방향 탐색
                for r in range(1, 51):           # 범위 탐색
                    for k in range(r+1):         # 범위 내에서 가로, 세로 조절하며 탐색
                        p, q = i + k*di[d] + 32768, j + (r-k)*dj[d] + 32768         # 새로운 좌표 범위 보정
                        if 0 <= p < 65536 and 0 <= q < 65536 and beer[p][q] == 0:   #
                            if [p, q] in Conv:
                                beer[p][q] = 19
                            else:
                                beer[p][q] = beer[i][j] - 1

    if beer[Rock[0]][Rock[1]] != 0:
        print('happy')
    else:
        print('sad')
'''