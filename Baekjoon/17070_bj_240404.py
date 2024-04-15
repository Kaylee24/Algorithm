import sys
input = sys.stdin.readline

N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]   # 0 : 빈칸, 1 : 벽
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for i in range(N):
    for j in range(1, N):
        if houses[i][j] == 0:
            r, c, d = dp[i][j]
            if r > 0:
                if j+1 < N and houses[i][j+1] == 0:
                    dp[i][j+1][0] += r
                    if i+1 < N and houses[i+1][j+1] == 0 and houses[i+1][j] == 0:
                        dp[i+1][j+1][2] += r
            if c > 0:
                if i+1 < N and houses[i+1][j] == 0:
                    dp[i+1][j][1] += c
                    if j+1 < N and houses[i+1][j+1] == 0 and houses[i][j+1] == 0:
                        dp[i+1][j+1][2] += c
            if d > 0:
                if j+1 < N and houses[i][j+1] == 0:
                    dp[i][j+1][0] += d
                if i+1 < N and houses[i+1][j] == 0:
                    dp[i+1][j][1] += d
                    if j+1 < N and houses[i+1][j+1] == 0 and houses[i][j+1] == 0:
                        dp[i+1][j+1][2] += d

print(sum(dp[N-1][N-1]))