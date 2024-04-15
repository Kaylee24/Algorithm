import sys
input = sys.stdin.readline

T = int(input())       # 테스트케이스의 수 T
for _ in range(T):
    N = int(input())   # 비밀번호의 길이 N

    keypad = [[7], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], [0, 4, 8], [5, 7, 9], [6, 8]]
    dp = [[0] * 10 for _ in range(N)]
    dp[0] = [1] * 10
    for i in range(1, N):
        for j in range(10):
            for k in keypad[j]:
                dp[i][j] += dp[i-1][k]
        if min(dp[i]) >= 1234567:
            for p in range(10):
                dp[i][j] %= 1234567

    print(sum(dp[N-1]) % 1234567)