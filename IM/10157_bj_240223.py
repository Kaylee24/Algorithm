C, R = map(int, input().split())   # 가로 C, 세로 R / (x, y)
K = int(input())

if C * R < K:   # 주어진 번호가 좌석 수보다 클 때
    print(0)
else:           # 주어진 번호가 좌석 수 이하일 때
    hall = [[0] * C for _ in range(R + 1)]    # 공연장 설정

    dt = [[-1, 0], [0, 1], [1, 0], [0, -1]]   # i, j 방향 설정 변수 설정
    i = R
    j = 0



    print(j, i)