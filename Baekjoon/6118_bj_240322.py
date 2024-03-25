import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())   # 헛간의 개수 N, 양방향 길 M개
adjl = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    adjl[A].append(B)
    adjl[B].append(A)

queue = deque([1])
visited = [0] * (N+1)
visited[1] = 1
maximum = 0
while queue:
    now = queue.popleft()
    for to in adjl[now]:
        if visited[to] == 0:
            visited[to] = visited[now] + 1
            queue.append(to)
            if maximum < visited[to]:
                maximum = visited[to]

print(visited.index(maximum), maximum-1, visited.count(maximum))