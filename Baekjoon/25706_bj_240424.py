import sys
input = sys.stdin.readline

N = int(input())
heights = [0] + list(map(int, input().split()))

dp = [1] * (N+1)
for i in range(N-1, 0, -1):
    if i + heights[i] < N:
        dp[i] = dp[i + heights[i] + 1] + 1
print(*dp[1:N+1])