N = int(input())
data = [list(input()) for _ in range(N)]   # str 으로 받음
village = [[0] * N for _ in range(N)]
num = 0
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
house = []

for i in range(N):
    for j in range(N):
        if data[i][j] == '1' and village[i][j] == 0:   # 집이면서, 단지로 체크하지 않은 경우
            stack = [[i, j]]
            num += 1
            village[i][j] = num
            h = 1
            while stack:
                p, q = stack.pop()
                for k in range(4):
                    y, x = p + di[k], q + dj[k]
                    if 0 <= y < N and 0 <= x < N and data[y][x] == '1' and village[y][x] == 0:
                        village[y][x] = num
                        h += 1
                        stack.append([y, x])
            house.append(h)

print(num)
house.sort()
for i in range(num):
    print(house[i])