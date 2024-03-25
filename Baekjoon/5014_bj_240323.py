from collections import deque

F, S, G, U, D = map(int, input().split())   # 총 F층, 스타트링크 G층, 강호 S층, 위로 U층, 아래로 D층 이동 가능
                                            # (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000)
if S == G:
    print(0)
else:
    queue = deque([S])
    visited = [-1] * (F+1)
    visited[S] = 0
    while queue:
        now = queue.popleft()
        if now == G:
            break

        for i in [U, -D]:
            if 1 <= now + i <= F and visited[now + i] == -1:
                visited[now + i] = visited[now] + 1
                queue.append(now + i)

    if visited[G] == -1:
        print('use the stairs')
    else:
        print(visited[G])