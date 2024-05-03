import sys
input = sys.stdin.readline

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if dp[i][j]:
            jump = numbers[i][j]

            if jump == 0:
                continue
            if i + jump < N:
                dp[i + jump][j] += dp[i][j]
            if j + jump < N:
                dp[i][j + jump] += dp[i][j]

print(dp[-1][-1])