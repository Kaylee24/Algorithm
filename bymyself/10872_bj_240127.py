# 0 <= N <= 12
N = int(input())

# N! 구하기
ans = 1
for i in range(1, N + 1):
    ans *= i

# N! 출력하기
print(ans)