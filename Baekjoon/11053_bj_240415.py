N = int(input())                      # 수열 A의 크기 N
A = list(map(int, input().split()))   # 수열 A
dp = [1] * N

for i in range(N):
    for k in range(N-i):
        if A[i] < A[i+k]:
            dp[i+k] = max(dp[i+k], dp[i]+1)

print(max(dp))