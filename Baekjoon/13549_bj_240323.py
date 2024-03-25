from collections import deque

N, K = map(int, input().split())   # 수빈이가 있는 위치 N, 동생이 있는 위치 K
if N == K:
    exit(print(0))
queue = deque([N])
visited = [-1] * 100001
visited[N] = 0
while queue:
    X = queue.popleft()
    if X == K:
        exit(print(visited[X]))

    if 0 <= X*2 <= 100000 and (visited[X*2] == -1 or visited[X*2] > visited[X]):
        visited[X*2] = visited[X]
        queue.appendleft(X*2)
    for i in [X+1, X-1]:
        if 0 <= i <= 100000 and visited[i] == -1:
            visited[i] = visited[X]+1
            queue.append(i)