from collections import deque

N, M, R = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

queue = deque([R])
visited = [0] * (N+1)
visited[R] = 1
cnt = 2

while queue:
    now = queue.popleft()
    graph[now].sort()

    for i in graph[now]:
        if visited[i]:
            continue

        queue.append(i)
        visited[i] = cnt
        cnt += 1

for i in range(1, N+1):
    print(visited[i])