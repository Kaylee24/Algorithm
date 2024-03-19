import sys
input = sys.stdin.readline

N = int(input())   # 도시의 개수
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

c, c_oil, total = 0, oil[0], 0
while c < N-1:
    if oil[c] < c_oil:
        c_oil = oil[c]
    total += road[c] * c_oil
    c += 1

print(total)