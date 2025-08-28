import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

N, M, R = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for i in range(1, N + 1):
    g[i].sort(reverse=True)  # 문제 조건이 내림차순이라면 유지

visited = [False] * (N + 1)
way = [0] * (N + 1)
cnt = 1

def dfs(u):
    global cnt
    visited[u] = True
    way[u] = cnt
    cnt += 1
    for v in g[u]:
        if not visited[v]:
            dfs(v)

dfs(R)

for i in range(1, N + 1):
    print(way[i])
