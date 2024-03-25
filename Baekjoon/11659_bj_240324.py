import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
S = sum(num)
quest = [list(map(int, input().split())) for _ in range(M)]

for i, j in quest:
    if i == j:
        print(num[i-1])
    elif j-i+1 <= N//2:
        print(sum(num[i-1:j]))   # index 는 X번째 수보다 1이 작기 때문에 보정해준다.
    else:
        print(S - (sum(num[:i-1]) + sum(num[j:])))