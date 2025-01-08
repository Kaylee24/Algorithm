import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * 1001

for i in range(N-1, -1, -1):
    dp[arr[i]] = max(dp[:arr[i]]) + 1

print(max(dp))