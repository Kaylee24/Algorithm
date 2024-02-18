N, M = map(int, input().split())   # 유저의 수 N, 친구 관계의 수 M
friend = [list(map(int, input().split())) for _ in range(M)]   # 친구 관계 정보

adjl = [[] for _ in range(N + 1)]   # 인접리스트, 무향그래프
for friendship in friend:
    adjl[friendship[0]].append(friendship[1])
    adjl[friendship[1]].append(friendship[0])

kevin = []   # 케빈 베이컨의 수 담을 리스트, 최종 출력 시 index 보정 필요

# bfs
for n in range(1, N + 1):   # '내'가 친구들한테 가는 수
    q = [n]          # 시작점 작업 대상 리스트에 추가
    visited = [0] * (N + 1)
    visited[n] = 1   # 시작점 방문 표시
    while q:
        t = q.pop(0)   # 작업 대상 확인요
        for f in adjl[t]:
            if visited[f] == 0:
                q.append(f)
                visited[f] = visited[t] + 1
    kevin.append(sum(visited))   # 사람 출력이라서 횟수의 대소관계만 파악하면 됨

print(kevin.index(min(kevin)) + 1)