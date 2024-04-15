import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())                                             # 이닝 수 N(2 ≤ N ≤ 50)
data = [[0] + list(map(int, input().split())) for _ in range(N)]   # 각 선수가 각 이닝에서 얻는 결과
possible_lineup = list(permutations(list(range(2, 10)), 8))
L = len(possible_lineup)

max_point = 0

for i in range(L):

    lineup = list(possible_lineup[i])
    lineup.insert(3, 1)

    point = 0
    n = 0
    p = 0
    while n < N:         # 주어진 이닝이 끝날때까지
        out_count = 0    # 새 이닝이 시작되면 out 수는 0으로 초기화된다.
        base = [0] * 3   # base 도 새로 시작한다.

        while out_count < 3:   # out count 가 3이 되면 해당 이닝을 종료한다.
            player = data[n][lineup[p]]

            if player == 0:          # 아웃이라면,
                out_count += 1
            elif player == 1:
                if base[2] == 1:
                    point += 1
                base = [1] + base[0:2]
            elif player == 2:
                point += base[1:3].count(1)
                base = [0, 1, base[0]]
            elif player == 3:
                point += base.count(1)
                base = [0, 0, 1]
            elif player == 4:
                point += base.count(1) + 1
                base = [0] * 3
            p += 1
            if p == 9:
                p = 0
        n += 1
    if point > max_point:
        max_point = point

print(max_point)