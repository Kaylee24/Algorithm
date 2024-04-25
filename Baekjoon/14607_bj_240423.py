N = int(input())

if N == 1:
    print(0)
else:
    result = 1
    for i in range(N-2):
        result += i+2
    print(result)



'''
[명시적인 코드(부분 / N == 1인 경우 없음)]
N = int(input())

result = 1
for i in range(3, N+1):
    result += i-1
print(result)
'''



'''
[메모리 초과 코드]
N = int(input())

dp = [0] * (N+1)
dp[2] = 1
for i in range(3, N+1):
    x = i//2
    dp[i] = dp[x] + dp[i-x] + x * (i-x)
print(dp[N])
'''