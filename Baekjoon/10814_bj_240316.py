N = int(input())                                               # 회원의 수
member = [list(map(str, input().split())) for _ in range(N)]   # 나이, 이름

member.sort(key=lambda x: int(x[0]))
for i in range(N):
    print(*member[i])