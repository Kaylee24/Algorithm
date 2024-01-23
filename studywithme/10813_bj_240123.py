# 바구니 N개, 교환 M번 / 1 <= N, M <= 100
N, M = map(int, input().split())

# 초기 공 순서 설정
balls = []
for n in range(1, N + 1):
    balls.append(n)

# print(balls)

# 공 교환, index는 0부터 시작하기 때문에 14번째 줄에서 i-1, j-1
for m in range(M):
    i , j  = map(int, input().split())
    balls[i - 1], balls[j - 1] = balls[j - 1], balls[i - 1]

# !출력 형태 주의!
print(*balls)