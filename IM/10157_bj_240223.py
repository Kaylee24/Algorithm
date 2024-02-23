C, R = map(int, input().split())   # 가로 C, 세로 R / (x, y)
K = int(input())

if C * R < K:
    print(0)
else:

    hall = [[0] * C for _ in range(R + 1)]



    dx = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    i = R
    j = 0
    hall[i][j] = 1
    while K > 0:                            # 주어진 수만큼 관객을 앉힌다.
        for k in range(4):
            while (0 <= i + dx[k][0] < R) and (0 <= j + dx[k][1] < C):
                i += dx[k][0]
                j += dx[k][1]
                hall[i][j] = 1
                K -= 1

    print(j, i)