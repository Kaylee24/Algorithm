N = int(input())
maze = list(map(int, input().split()))

if N == 1:
    exit(print(0))

dp = [float('inf')] * N
for i in range(N-1, -1, -1):
    if maze[i] > 0:
        x = i + maze[i]
        if x >= N-1:
            dp[i] = 1
        else:
            dp[i] = min(dp[i+1:x+1]) + 1

if dp[0] == float('inf'):
    print(-1)
else:
    print(dp[0])