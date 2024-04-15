'문제 꼼꼼히 읽을 것'

import sys
input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]

# 산술평균 / 소수점 이하 첫째 자리에서 반올림한 값
print(round(sum(num)/N))

# 중앙값
num.sort()
print(num[N//2])

# 최빈값 / 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
max_cnt = {}
for i in set(num):
    i_cnt = num.count(i)
    if i_cnt not in max_cnt:
        max_cnt[i_cnt] = [i]
    else:
        max_cnt[i_cnt].append(i)

result = max_cnt[(max(max_cnt.keys()))]
if len(result) == 1:
    print(result[0])
else:
    result.sort()
    print(result[1])

# 범위
print(max(num)-min(num))