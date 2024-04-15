import sys
input = sys.stdin.readline

N = int(input())
consults = [list(map(int, input().split())) for i in range(N)]   # 날짜, T, P
dp = [0] * (N+1)

for i in range(N-1, -1, -1):   # 상담 정보를 거꾸로 순회하면서
    time, pay = consults[i]

    if i + time <= N:
        dp[i] = max(dp[i + time] + pay, dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])