'20:40 / 목표 21:20 (3/3) / ~ 21:04'

'''
N개의 노드로 이루어진 트리가 주어지고 M개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.

M개의 줄에 차례대로 입력받은 두 노드 사이의 거리를 출력한다.
'''

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())                               # 노드의 개수 N, 거리를 알고 싶은 노드 쌍의 개수 M
data = [list(map(int, input().split())) for _ in range(N-1)]   # 트리 상에 연결된 두 점과 거리
quest = [list(map(int, input().split())) for _ in range(M)]    # 거리를 알고 싶은 M개의 노드 쌍

# 1. 트리를 그린다. : 연결된 노드와 거리 정보 담기
# 2. bfs 탐색을 통해 노드 간의 거리를 구한다.

# tree 그리기
tree = [[] for _ in range(N+1)]   # 노드 번호가 1부터 N까지 이므로 index 보정을 위해 원소 리스트는 1개 더 만들어준다.
for d in data:
    tree[d[0]].append((d[1], d[2]))
    tree[d[1]].append((d[0], d[2]))
for t in tree:
    t.sort(key=lambda x: x[0])

# 거리를 알고자 하는 노드 정보 정렬
for q in quest:
    q.sort()

# bfs 탐색 시행
for q in quest:
    queue = deque([q[0]])
    finish = q[1]
    visited = [-1] * (N+1)
    visited[q[0]] = 0
    while queue:
        now = queue.popleft()
        if now == finish:
            print(visited[finish])
            break
        for to in tree[now]:                            # 현재 노드에서 갈 수 있는 노드들을 순회하며
            if visited[to[0]] == -1:                    # 아직 방문하지 않은 노드라면
                visited[to[0]] = visited[now] + to[1]   # 방문 표시 겸 거리 표시
                queue.append(to[0])                     # 작업 리스트에 도착지 추가