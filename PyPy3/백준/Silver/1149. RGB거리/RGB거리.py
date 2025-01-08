import sys
input = sys.stdin.readline

N = int(input())
costs = [0] * N
for i in range(N):
    costs[i] = list(map(int, input().split()))

dp = [costs[0]] + [0] * (N-1)
for i in range(1, N):
    dp[i] = [costs[i][0] + min(dp[i-1][1:]), costs[i][1] + min(dp[i-1][0], dp[i-1][2]), costs[i][2] + min(dp[i-1][:2])]

print(min(dp[-1]))